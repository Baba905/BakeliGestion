from curses import wrapper
from tokenize import group
from django.http import HttpRequest
from django.shortcuts import redirect



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groupe =None
            if request.user.groups.exist():
                groupe = request.user.groups.all()[0]
            if groupe in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpRequest("Not allowed to connect to this page")
        return wrapper_func 
    return decorator