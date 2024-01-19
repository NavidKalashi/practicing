from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book

class PublisherListView(ListView):
    model = Publisher
    
class PublisherDetailView(DetailView):
    model = Publisher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context