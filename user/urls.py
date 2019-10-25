from django.urls import path
from .views import SignUp, AuthView

urlpatterns = [
    path('', SignUp.as_view()),
    path('/auth', AuthView.as_view()),
]


