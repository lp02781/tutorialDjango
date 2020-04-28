# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'about',
        'heading':'about',
        'subheading':'tentang'
    }
    return render(request,'about/index.html',context)
