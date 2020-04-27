from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import VoteForm, CommentForm
from .models import Vote, Comment
from django.db.models import Max
from random import randint


# Create your views here.
def index(request):
    votes = Vote.objects.order_by('-pk')
    context = {
        'votes': votes
    }
    return render(request, 'votes/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('votes:index')
    else:
        form = VoteForm()
    context = {
        'form': form
    }
    return render(request, 'votes/create_vote.html', context)


def detail(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    comments = Comment.objects.filter()
    form = CommentForm()
    context = {
        'vote': vote,
        'form': form,
    }
    return render(request, 'votes/detail.html', context)


@require_POST
@login_required
def create_comment(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.vote = vote
        comment.save()
    return redirect('votes:detail', vote_pk)


@require_POST
@login_required
def delete_comment(request, vote_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('votes:detail', vote_pk)


def random(request):
    max_id = Vote.objects.all().aggregate(max_id=Max("pk"))['max_id']
    while True:
        idx = randint(1, max_id)
        if Vote.objects.get(pk=idx):
            return redirect('votes:detail', idx)
