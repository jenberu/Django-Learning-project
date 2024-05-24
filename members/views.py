from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers=Member.objects.all().values()
    templet=loader.get_template('all_members.html')
    context={
        'mymembers':mymembers
    }
    return HttpResponse(templet.render(context))

# Create your views here.
