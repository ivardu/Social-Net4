from django.shortcuts import render
from users.forms import UserRegForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.


class UserRegView(FormView):
	template_name = 'users/register.html'
	form_class = UserRegForm
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)