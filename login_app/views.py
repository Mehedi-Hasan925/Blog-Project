from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from login_app import forms

# Create your views here.
def sign_up(request):
    registered = False
    form = forms.signup_form()
    if request.method == 'POST':
        form = forms.signup_form(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    diction = {'registered':registered, 'form':form}
    return render(request,'login_app/sign_up.html', context=diction)



def Sign_in(request):
    
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    
    return render(request,'login_app/sign_in.html',context={'form':form})


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile_page(request):
    
    diction={}
    return render(request,'login_app/profile.html',context=diction)

@login_required
def edit_profile_information(request):
    current_user = request.user
    form = forms.UserProfileChange(instance=current_user)

    if request.method == 'POST':
        form = forms.UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = forms.UserProfileChange(instance=current_user)
    
    diction = {'form':form}
    return render(request,'login_app/update_profile.html',context=diction)

@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    
    return render(request,'login_app/pass_change.html',context={'form':form,'changed':changed})


@login_required
def add_pro_pic(request):
    current_user = request.user
    form = forms.change_profile_pic()
    if request.method == 'POST':
        form=forms.change_profile_pic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = current_user
            user_obj.save()
            HttpResponseRedirect(reverse('login_app:profile'))
    diction = {'form':form}
    return render(request,'login_app/profile_pic_add.html',context=diction)

@login_required
def change_pro_pic(request):
    current_user = request.user
    form = forms.change_profile_pic(instance=current_user.user_profile)
    if request.method == 'POST':
        form = forms.change_profile_pic(request.POST, request.FILES, instance=current_user.user_profile)
        if form.is_valid():
            form.save()
            HttpResponseRedirect(reverse('login_app:profile'))
    diction = {'form':form}
    return render(request,'login_app/profile_pic_add.html',context=diction)