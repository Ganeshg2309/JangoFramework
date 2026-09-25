from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PlayListForm
from .forms import SongRequestForm


def view1(request):
    form=PlayListForm()
    form1=SongRequestForm()
  
    playlist = [
    {'title': 'BbY WOW', 'plays': 33059939, 'album': 'NO ME ARREPIENTO DE SENTIR TANTO'},
    {'title': 'Beauty And A Beat', 'plays': 23060351, 'album': 'Believe'},
    {'title': 'Earrings', 'plays': 22481881, 'album': 'Sweet Boy'},
    {'title': 'Loser', 'plays': 22170033, 'album': 'Deadbeat'},
    {'title': 'The One That Got Away', 'plays': 22169158, 'album': 'Teenage Dream'},
    {'title': 'Dai Dai', 'plays': 21507155, 'album': 'Dai Dai'},
    {'title': 'Self Aware', 'plays': 20891173, 'album': 'Self Aware'},
    {'title': 'the cure', 'plays': 19826357, 'album': 'you seem pretty sad for a girl so in love'},
    {'title': 'Babydoll', 'plays': 19450905, 'album': "Don't Forget About Me, Demos"},
    {'title': 'back to friends', 'plays': 19424543, 'album': 'I Barely Know Her'},
    {'title': 'Billie Jean', 'plays': 19044517, 'album': 'Thriller'}
    ]

    # return render(request,"playlist/playlist_details.html",{"playlist":playlist})

    return render(request ,"playlist/playlist_details.html",{"form":form,"playlist":playlist,"form1":form1})
