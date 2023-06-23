from django.urls import path

from .views import CurrentDateView, RandomNumber, HelloWorld, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('random/', RandomNumber.as_view()),
    path('hello/', HelloWorld.as_view())
]
