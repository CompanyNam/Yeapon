from django.shortcuts import render
from django.shortcuts import redirect
from .userform import RegisterForm
# Create your views here.
from .userform import LoginForm
from django.contrib.auth import authenticate ,login

def login_view(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('app:index')
    return render(request, 'accounts/account.html' ,{'form':form , 'title':'Log IN'})
def register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username ,password=password)
        login(request, new_user)
        return redirect('app:index')
    return render(request, 'accounts/account.html', {'form':form , 'title': 'REGISTER'})

