from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def playlist(request):
    return HttpResponse('''<h1>my play list</h1><a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'>harry vediosss</a><br>
    <a href='https://www.youtube.com/channel/UC0wao-qtsBkt5dDE6R6xnDw/playlists'>got</a>''')