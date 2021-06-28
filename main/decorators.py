from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test



def UnauthenticatedUser(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request)
    return wrapper



def is_moderator(func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Moderator').exists():
            return func(request, *args, **kwargs) 
        else:
            return redirect('home')
    return wrapper