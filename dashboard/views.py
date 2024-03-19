from django.shortcuts import render

def dashboard(request):
    context={
        'title': 'Dashboard',
    }

    return render(request, 'html/dashboard/main.html', context)

def calendar(request):
    context={
        'title': 'Calendar',
    }

    return render(request, 'html/dashboard/calendar.html', context)

def entry(request,date,reference):
    context={
        'title': f'Entry on {date}',
    }

    return render(request, 'html/dashboard/entry.html', context)