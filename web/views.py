from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Message

class MessageList(ListView):
    model = Message
    ordering = ['-id'] #change -id into -score

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']
    success_url = reverse_lazy('msg_list')

class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')
    
# Create your views here.

