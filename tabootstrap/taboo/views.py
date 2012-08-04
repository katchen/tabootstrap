from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def instructions(request):
    return render_to_response('instructions.html')

def play(request):
    if request.is_ajax():
        pass
    return render_to_response('play.html')