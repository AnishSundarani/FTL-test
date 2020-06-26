from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('api/getdata/')
    return response