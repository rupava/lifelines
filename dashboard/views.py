from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Entry

@login_required
def dashboard(request):
    context={
        'title': 'Dashboard',
    }

    return render(request, 'html/dashboard/main.html', context)

@login_required
def calendar(request):
    context={
        'title': 'Calendar',
    }

    return render(request, 'html/dashboard/calendar.html', context)

@login_required
def entry(request,dateEntry):
    if request.method == 'GET':
        context = {}
        # Check if the date is a valid date object
        try:
            formated_date = datetime.strptime(dateEntry, '%Y-%m-%d')
        except ValueError:
            raise Http404
        
        try:
            entryObj = Entry.objects.get(user = request.user, date = formated_date)
            context.update({
                'state':True,
            })
        except ObjectDoesNotExist as e:
            context.update({'state':False})
        context.update({
            'title': f'Entry for {dateEntry}',
            'entry_date': dateEntry,
        })

    return render(request, 'html/dashboard/entry.html', context)