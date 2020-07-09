from django.shortcuts import render,redirect
from .forms import UserOurRegistation
from django.contrib import messages

def register(request):
    if request.method =="POST":
        form = UserOurRegistation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Пользователь {username} был успешно создан!')
            return redirect('blog-home')
    else:
        form = UserOurRegistation()
    return render(request,'users/registration.html',{'form':form,'title': 'Регистрация пользователя'})