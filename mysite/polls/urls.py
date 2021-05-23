from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #polls/
    path('', views.index, name='index'),
    #polls/5/detail/
    path('<int:question_id>/detail/', views.detail, name='detail'),
    #polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
