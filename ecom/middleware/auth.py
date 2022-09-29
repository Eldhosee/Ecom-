from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect


def auth_middleware(get_response):
    
    def middleware(request):
        if not request.session.get('user_id'):
            return redirect('login')

        response = get_response(request)

        return response

    return middleware