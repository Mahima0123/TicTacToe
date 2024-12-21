from django.shortcuts import render, get_object_or_404, redirect
from .models import Game

def index(request):
    game, created = Game.objects.get_or_create(pk=1)
    print(f"Game board: {game.board}")
    return render(request, 'game/index.html', {'game': game})

def make_move(request, position):
    print(f"Move made at position: {position}")
    game = get_object_or_404(Game, pk=1)
    game.make_move(int(position))
    return redirect('index')

def restart_game(request):
    game = get_object_or_404(Game, pk=1)
    game.board = ' ' * 9
    game.current_turn = 'X'
    game.winner = None
    game.save()
    return redirect('index')
