# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile
from django.shortcuts import render

# Create your views here.
def index(request):
    items = Profile.objects.all()
    context = {
        'items': items
    }
    print(context)
    return render(request, 'index.html',context)
