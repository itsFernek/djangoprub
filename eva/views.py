from django.shortcuts import render


def home(request):
    context = {}
    template = 'ate.html'
    return render(request, template, context)