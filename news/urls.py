from django.urls import path, include
from django.views.generic import ListView, DetailView
from news.models import Notes

urlpatterns = [
    path('', ListView.as_view(queryset=Notes.objects.values('created_on').order_by('-created_on')[:5], template_name="/LibSite/notes.html")),
    path('/<int:pk>', DetailView.as_view(model = Notes, template_name = 'LibSite/NewsPage.html')),
]