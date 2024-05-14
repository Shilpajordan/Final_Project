from django.http import HttpResponseBadRequest, HttpResponse 
from .chatbot_logic import chat_bot  
from django.shortcuts import render

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = chat_bot(user_input)
        return HttpResponse(response)
    else:
        return HttpResponseBadRequest('This endpoint only accepts POST requests.')
    

def index_view(request):
    return render(request, 'index.html')
