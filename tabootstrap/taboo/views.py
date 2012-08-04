from django.shortcuts import render_to_response
from django.template import RequestContext
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
    
def create_word(request):
    if request.method == 'POST':
        taboo_word = str(request.POST['word'])
        taboo_query = TabooWord.objects.filter(word=taboo_word)
        if taboo_query:
            taboo_model = taboo_query[0]
            taboo_model.banned_words.all().delete()
        else:
            taboo_model = TabooWord.objects.create(word=taboo_word)   
        banned_words = request.POST.getlist('banned_word')
        banned_words = [str(word) for word in banned_words]
        for ban in banned_words:
            ban_query = BannedWord.objects.filter(word=ban)
            if ban_query:
                ban_inst = ban_query[0]
            else:
                ban_inst = BannedWord.objects.create(word=ban)
            taboo_model.banned_words.add(ban_inst)
        return render_to_response('message.html',{'message':'hooray!'})
        #tabform = TabooWordForm(request.POST)
        #banform = BannedWordFormSet(request.POST)
    else:
        tabform = TabooWordForm()
        banform = BannedWordFormSet()
        return render_to_response('createword.html',{'tabform':tabform, 'banform':banform},context_instance=RequestContext(request))
