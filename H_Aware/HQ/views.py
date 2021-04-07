from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John',
        'title' : 'Blog Post',
        'content' : 'First Post',
        'date_posted' : 'June 27,2021'
    },
    {
        'author': 'Jill',
        'title' : 'Blog Post2',
        'content' : 'Second Post',
        'date_posted' : 'June 20,2021'
    }
]

# Create your views here.
def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'HQ/home.html', context)

def about(request):
    return render(request, 'HQ/about.html', {'title': 'About'})