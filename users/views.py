from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from users.forms import UserUpdateForm, UserRegForm, ProfileForm, FriendReqForm
from users.models import SnetUser, Friends
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

# Sign Up Registration View
class UserRegView(FormView):
	template_name = 'users/register.html'
	form_class = UserRegForm
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

# Own profile details of the logged in user
@login_required
def profile(request):

	if request.method == 'POST':
		pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		uform = UserUpdateForm(request.POST, instance=request.user)
		fform = FriendReqForm(request.POST)
		if pform.is_valid() and uform.is_valid():
			pform.save()
			uform.save()

			return HttpResponseRedirect(reverse('profile'))
	else:
		pform = ProfileForm(instance=request.user.profile)
		uform = UserUpdateForm(instance=request.user)
		# Filtering the user list based on the friend request 
		recieved_frn_req_set = Friends.objects.filter(auser_id=request.user.id).filter(friends='No')
		# Verifying the friend request
		if recieved_frn_req_set:
			count = recieved_frn_req_set.count()
			frn_req_list = []
			for obj in recieved_frn_req_set:
				frn_req_list.append(obj.ruser)		

	return render(request, 'users/profile.html',locals())

# Read only profile
@login_required
def rprofile(request, id):
	user_obj = SnetUser.objects.get(pk=id) #Read only profile User
	form = UserUpdateForm(instance=user_obj)
	#  Filtering the Friends list 
	friends_yes_r = Friends.objects.filter(friends='yes').filter(ruser=request.user).filter(auser_id=id)
	friends_yes_a = Friends.objects.filter(friends='yes').filter(ruser=user_obj).filter(auser_id=request.user.id)
 	#  If the users are friends
	if friends_yes_r:
		accepted = friends_yes_r[0]
	elif friends_yes_a:
		accepted = friends_yes_a[0]
		


	# If logged in user verifying any one's rprofile and if he sent Friend Req Sent
	f_r_s = Friends.objects.filter(friend_req_sent='yes').filter(ruser=request.user)
	# If Read only user has sent the logged in user friend request
	f_r_s_r = Friends.objects.filter(friend_req_sent='yes').filter(ruser=user_obj)
	if f_r_s:
		for obj in f_r_s:
			# Verifying the Read only profile user and Friends Accepting User
			if user_obj.id == obj.auser_id:
				sent = obj.friend_req_sent
				auser = SnetUser.objects.get(pk=obj.auser_id)
	if f_r_s_r:
		for obj in f_r_s_r:
			if obj.auser_id == request.user.id:
				sent = obj.friend_req_sent
				ruser = user_obj


	
	if request.method == 'POST':
		frform = FriendReqForm(request.POST)
		if frform.is_valid():
			frnds_model_obj = frform.save(commit=False)
			frnds_model_obj.friend_req_sent = frform.cleaned_data['friend_req_sent']
			frnds_model_obj.ruser = request.user
			frnds_model_obj.auser_id = id
			frnds_model_obj.save()
			return HttpResponseRedirect(reverse('rprofile',args=(id,)))
		
	else:
		frform = FriendReqForm()

	return render(request, 'users/rprofile.html', locals())


def friend_req(request):
	if request.method == 'POST':
		friend_obj = Friends.objects.filter(ruser_id=request.POST['item']).filter(auser_id=request.user.id)
		friend_model_obj = friend_obj[0]
		friend_model_obj.friends = request.POST['friends']
		friend_model_obj.save()

		return HttpResponseRedirect(reverse('profile'))