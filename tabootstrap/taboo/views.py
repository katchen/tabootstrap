from django.shortcuts import render_to_response
from django.http import HttpResponse
from taboo.models import *
import random
import json

def index(request):
    return render_to_response('index.html')

def instructions(request):
    return render_to_response('instructions.html')

def play(request):
    if request.method=="GET" and request.is_ajax():
        data = {'used_all':False}

        prev_words = request.GET['prev_words']
        prev_list = str(prev_words).split(",")
        taboo_words = TabooWord.objects.exclude(word__in=prev_list)
        if taboo_words.exists() == False:
            taboo_words = TabooWord.objects.all()
            data['used_all'] = True
        taboo_word = random.choice(taboo_words)
        taboo_string = taboo_word.word
        banned_words = taboo_word.banned_words.all()
        banned_list = []
        for ban in banned_words:
            banned_list.append(ban.word)

        data['taboo_word'] = taboo_string
        data['banned_words'] = banned_list
        data = json.dumps(data)
        return HttpResponse(data)

    return render_to_response('play.html')