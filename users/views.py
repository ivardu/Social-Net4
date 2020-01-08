from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from users.forms import UserUpdateForm, UserRegForm, ProfileForm
from users.models import SnetUser
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


class UserRegView(FormView):
	template_name = 'users/register.html'
	form_class = UserRegForm
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

@login_required
def profile(request):

	if request.method == 'POST':
		pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		uform = UserUpdateForm(request.POST, instance=request.user)
		if pform.is_valid() and uform.is_valid():
			pform.save()
			uform.save()
			return HttpResponseRedirect(reverse('profile'))
	else:
		pform = ProfileForm(instance=request.user.profile)
		uform = UserUpdateForm(instance=request.user)

	return render(request, 'users/profile.html',locals())

@login_required
def rprofile(request, id):
	user_obj = SnetUser.objects.get(pk=id)
	form = UserUpdateForm(instance=user_obj)

	return render(request, 'users/rprofile.html', locals())