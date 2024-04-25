from django.shortcuts import render


def home(request):
    return render(request, 'doc_search/index.html')


def login(request):
    return render(request, 'doc_search/login.html')
