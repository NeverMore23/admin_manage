from django.shortcuts import render, redirect
from .models import User
from rbac.service.init_permission import init_permission


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            init_permission(request, user)
            return redirect('/index/')
        return render(request, 'login.html', {'msg': '用户名或密码错误'})
