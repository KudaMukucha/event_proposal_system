from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages
from .form import UpdateProfileForm
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
#login users
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request,f'You are logged in as {user}')
                return redirect('home')
            else:
                return redirect('account-block')
        else:
            messages.warning(request,'Invalid username or password.')
            return render(request,'accounts/login.html',{'username':username})
    else:
        return render(request,'accounts/login.html')

#logout users
def logout_user(request):
    logout(request)
    messages.success(request,'Your active session has ended. Log in to continue.')
    return redirect('login')


#update info
def update_profile(request):
    if request.method =='POST':
        form = UpdateProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully.')
            return redirect('home')
        else:
            messages.warning(request,'Oops, something went wrong!')
            return redirect('update-profile')
    else:
        form = UpdateProfileForm(instance=request.user)
        return render(request,'accounts/update-profile.html',{'form':form})

#change password 
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password has been changed successfully.')
            return redirect('home')
        else:
            messages.warning(request,'Oops,something went wrong! Please try again.')
            return redirect('change-password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'accounts/change-password.html',{'form':form})
    
#account block
def account_block(request):
    return render(request,'accounts/account-block.html')