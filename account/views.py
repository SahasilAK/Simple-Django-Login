from django.shortcuts import render, redirect
from account.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def home(request):
    return render(request,'account/index.html')

def signupuser(request):

    context = {}
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        profile_form =UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            new_user = authenticate(username=request.POST.get('username'),
                                    password=request.POST.get('password'),
                                    )
            login(request, new_user)

            return redirect('home')


    else:
        context['user_form'] = UserForm()
        context['profile_form'] = UserProfileInfoForm()


    return render(request,'account/register.html',context)




def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('account:account_view')
            else:
                context['error'] = 'Account not active'
        else:

            context['error'] = 'Invalid login'


    return render(request,'account/login.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# @login_required
def account_view(request):

    context = {}




    return render(request,'account/account.html',context)
