# -*- coding: utf-8 -*-
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def lvs(request):
    users = User.objects.all()

    result = dict()
    for user in users:
        result[user.username] = user.password

    return HttpResponse(result)


def index(request):
    return HttpResponse("ok")


class AdminLoginView(LoginView):
    pass
