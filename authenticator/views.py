from django.shortcuts import render

def signup(request):
    context={
        'title': 'Landing',
    }
    
    return render(request, 'html/authenticator/signup.html', context)