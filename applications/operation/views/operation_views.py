# -*- coding: utf-8 -*-
from django.contrib.auth.views import LoginView
from django.http import HttpResponse


def lvs(request):
    return HttpResponse("ok")


def index(request):
    return HttpResponse("ok")


class AdminLoginView(LoginView):
    pass
