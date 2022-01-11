from django.urls import path

from . import views

urlpatterns = [
    path('wat', views.get_wat, name='wat'),
    path('srt', views.get_srt, name='srt'),

]