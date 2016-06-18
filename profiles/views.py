from django.shortcuts import render
from django.contrib.auth.views import login as django_login


def my_login(request):
    # do something
    res = django_login(request)

    return res

