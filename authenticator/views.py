from django.shortcuts import render

def signup(request):
    context={
        'title': 'Signup',
    }
    
    return render(request, 'html/authenticator/signup.html', context)