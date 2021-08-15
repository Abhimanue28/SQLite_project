from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.db.models import Avg


from .models import Game

# Create your views here.
def index(request):
    Games=Game.objects.all().order_by("title")
    num_games=Games.count()
    avg_rating=Games.aggregate(Avg("rating"))
    return render(request,"game_studio/index.html", {
        "games":Games,
        "game_count":num_games,
        "average_rating":avg_rating
    })

def game_detail(request,slug):
    #try:
       # book=Game.objects.get(pk=id)
    #except:
      # raise Http404()
    game=get_object_or_404(Game,slug=slug )
    return render(request,"game_studio/game_detail.html",{
            "title":game.title,
            "game_designer":game.game_designer,
            "rating":game.rating,
            "top_seller":game.top_seller

    })