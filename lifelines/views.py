from django.shortcuts import render

def home(request):
    
    context={
        'title': 'Landing',
    }
    
    return render(request, 'html/index.html', context)