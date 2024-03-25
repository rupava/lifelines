from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .tools import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Entry
import json

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

        formated_date = checkDate(dateEntry)
        if not formated_date:
            raise  Http404
        
        try:
            entryObj = Entry.objects.get(user = request.user, date = formated_date)
            context.update({
                'state':True,
                'data':entryObj,
            })

        except ObjectDoesNotExist as e:
            context.update({'state':False})

        context.update({
            'title': f'Entry for {dateEntry}',
            'entry_date': dateEntry,
        })
 
    if request.method == 'POST':
        formated_date = checkDate(dateEntry)
        if not formated_date:
            raise  Http404
        
        try:
            try:
                entryObj = Entry.objects.get(user = request.user, date = formated_date)
                entryObj.entry_title = request.POST.get('entry-title')
                entryObj.entry_content = request.POST.get('entry-content')
                entryObj.save()

                m_dat = "Your entry has been updated."
            except ObjectDoesNotExist:
                entryObj = Entry.objects.create(
                    user = request.user,
                    date = formated_date,
                    entry_title = request.POST.get('entry-title'),
                    entry_content = request.POST.get('entry-content'),
                )
                m_dat = "Your entry has been created."

        except Exception as e:
            m_dat = e
            print("Exception:>>>>>", e)
        messages.success(request, m_dat)
        return redirect(f'/dashboard/entry/{dateEntry}/')
        
    return render(request, 'html/dashboard/entry.html', context)

@login_required
def list_entries(request,date):
    user = request.user
    formated_date = checkYearMonth(date)

    if formated_date is False:
        return JsonResponse({"message":"Bad Request"},status=200, safe=False)

    if formated_date[0] == 1:
        entryObj =Entry.objects.filter(
            date__year=formated_date[1].year
            ).values('entry_title', 'date')

    elif formated_date[0] == 2:
        entryObj = Entry.objects.filter(
            date__month=formated_date[1].month,
            date__year=formated_date[1].year
        ).values('entry_title', 'date')

    res_data = list(entryObj.values('entry_title', 'date'))
    return JsonResponse(res_data, safe=False,status = 200)
