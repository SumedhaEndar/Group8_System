from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User
from .forms import TrainerSignUpForm, MemberSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import trainer_required

# Create your views here.
class TrainerSignUpView(CreateView):
    model = User
    form_class = TrainerSignUpForm
    template_name = 'users/trainer_signup.html'  # Adjust the template name as needed

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trainer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('trainer-home')


class MemberSignUpView(CreateView):
    model = User
    form_class = MemberSignUpForm
    template_name = 'users/member_signup.html'  # Adjust the template name as needed

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'member'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('member-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_member:
                return reverse('member-home')
            elif user.is_trainer:
                return reverse('trainer-home')
            elif user.is_admin:
                return reverse('admin-home')
            elif user.is_counter:
                return reverse('counter-home')
        else:
            return reverse('login')
