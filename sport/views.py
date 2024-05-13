from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Comment, Player, Team, News
from .forms import CommentForm 

def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'comment_detail.html', {'comment': comment})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_detail', comment_id=comment_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request, 'confirm_delete_comment.html', {'comment': comment})