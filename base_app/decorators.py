from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_groups = [group.name for group in request.user.groups.all()]
            if group_name in user_groups:
                return view_func(request, *args, **kwargs)
            else:
                # return HttpResponseForbidden("You don't have permission to access this page.")
                return render(request,'forbidden.html')
        return _wrapped_view
    return decorator