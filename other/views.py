from datetime import datetime
from random import random

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)


class RandomNumber(View):
    def get(self, request):
        random_number = random()
        return HttpResponse(random_number)


class HelloWorld(View):
    def get(self, request):
        html = """<h1>Hello, World</h1>"""
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')

