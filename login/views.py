from django.views import View
from django.shortcuts import render


class Login(View):
    def get(self, request):
        return render(request, 'login/index.html')