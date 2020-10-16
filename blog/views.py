from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Homepage of the website, first thing that a user sees

def homepage(request):
    context ={}
    return render(request, 'homepage.html', context)

class PostsList(ListView):
    model = Post
    tempalte_name = 'posts_list.html'