# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import randrange
from time import strftime

# Create your views here.

def index(request):
    return render(request, 'ninja_gold_app/index.html')

def process(request):
    if 'results' not in request.session:
        request.session['results'] = []
    my_result = request.session['results']
    if request.POST['building'] == 'farm':
        gold = randrange(10,20)
        message = "Earned " + str(gold) + " gold from the farm!"
        time = strftime('%B %d %Y %X')
        list_append = {
            'class': 'win',
            'message': message,
            'time': time 
        }
        my_result.append(list_append)
        request.session['results'] = my_result
        print request.session['results']
    if request.POST['building'] == 'cave':
        gold = randrange(5,10)
        message = "Earned " + str(gold) + " gold from the cave!"
        time = strftime('%B %d %Y %X')
        list_append = {
            'class': 'win',
            'message': message,
            'time': time 
        }
        my_result.append(list_append)
        request.session['results'] = my_result
        print request.session['results']
    if request.POST['building'] == 'house':
        gold = randrange(2,5)
        message = "Earned " + str(gold) + " gold from home!"
        time = strftime('%B %d %Y %X')
        list_append = {
            'class': 'win',
            'message': message,
            'time': time 
        }
        my_result.append(list_append)
        request.session['results'] = my_result
        print request.session['results']
    if request.POST['building'] == 'casino':
        gold = randrange(-50,50)
        if gold < 0:
            message = "Entered a casino and lost " + str(gold * -1) + " gold... Ouch..."
            my_class = "loss"
        else: 
            message = "Earned " + str(gold) + " gold at the casino!!"
            my_class = "win"
        time = strftime('%B %d %Y %X')
        list_append = {
            'class': my_class,
            'message': message,
            'time': time 
        }
        my_result.append(list_append)
        request.session['results'] = my_result
        print request.session['results']
    return redirect('/')
