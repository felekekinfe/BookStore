from django.shortcuts import render,redirect
from django.views.generic import  CreateView
from .models import Account
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.


class UserRegisterView(CreateView):
    form_class=RegistrationForm
    template_name='register.html'
    success_url=reverse_lazy('home')

class UserLoginView(LoginView):
    form_class=LoginForm
    template_name='userlogin.html'
    success_url=reverse_lazy('home')
   
    #     post_username = request.POST['username']
    #     post_password = request.POST['password']
    #     post_conf_password =request.POST['confirm_password']
    #     post_email = request.POST['email']
    #     post_phone =  request.POST['phone']
    #     post_first_name = request.POST['first_name']
    #     post_last_name = request.POST['last_name']
    #     check_username = Account.objects.all().filter(username=post_username)
    #     check_email = Account.objects.all().filter(email=post_email)
    #     check_phone = Account.objects.filter(phone=post_phone).exists()
    # else:
    #     if request.user.is_authenticated:
    #         return redirect('home')
    #     else:
    #         return render(request, 'register.html')