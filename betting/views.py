from django.shortcuts import render
# from django.httteap import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {

    'team1': 'Manu',
    'team1odds': '2.4',
    'team2': 'Chelsea',
    'team2odds': '1.6',
    'placed_bet': 'Manu',
    'odds_value': '2.4',
    'game_day': 'date',
    'history': 'Chelsea won',
    }

]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'betting/index.html', context)

def about(request):
    return render(request, 'betting/about.html')