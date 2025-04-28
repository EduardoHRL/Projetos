from django.shortcuts import redirect
from django.urls import reverse

class NavigationControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path == reverse('login') and request.COOKIES.get('rememberMe'):
            response['Cache-Control'] = 'private, max-age=3600'
        elif not request.user.is_authenticated:
            response['Cache-Control'] = 'no-store, must-revalidate'
        
        if request.user.is_authenticated and request.path == reverse('login'):
            return redirect('index')
            
        return response