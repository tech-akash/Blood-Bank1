from django.contrib.auth import decorators
from django.http import HttpResponse
from django.shortcuts import redirect

def un_authenticated(func_view):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func_view(request,*args, **kwargs)
    return wrapper

def allowed_user(allowedroles=[]):
    def decorator(func_view):
        def wrapper(request,*args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group  in allowedroles:
                return func_view(request,*args, **kwargs)
            else:
                if group== 'admin':
                    return redirect('admin1')
                else :
                    return redirect('home')
                    

        return wrapper
    return decorator
