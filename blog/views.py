from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Corey',
        'title': 'Sunday',
        'content': 'It\'s a beautifull day',
        'date': '14.06.2020'
    },
    {
        'author': 'Mia',
        'title': 'Saturday',
        'content': 'It\'s a very bad day',
        'date': '13.06.2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'Fish'})

