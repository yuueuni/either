from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import VoteForm, CommentForm
from .models import Vote, Comment
from django.db.models import Max
from random import choice


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
    opred = Comment.objects.filter(vote=vote.pk, pick='red').count()
    opblue = Comment.objects.filter(vote=vote.pk, pick='blue').count()
    form = CommentForm()
    if opred or opblue:
        opred, opblue = (opred/(opred+opblue))*100, (opblue/(opred+opblue))*100
    context = {
        'vote': vote,
        'form': form,
        'opred': opred,
        'opblue': opblue,
    }
    return render(request, 'votes/detail.html', context)


@login_required
def update(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    if request.user == vote.user:
        if request.method == 'POST':
            form = VoteForm(request.POST, instance=vote)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.user = request.user
                vote.save()
                return redirect('votes:detail', vote_pk)
        else:
            form = VoteForm(instance=vote)
        context = {
            'form': form
        }
        return render(request, 'votes/create_vote.html', context)
    else:
        return redirect('votes:index')


@require_POST
@login_required
def delete_vote(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    if request.user == vote.user:
        vote.delete()
    return redirect('votes:index')


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
    # max_id = Vote.objects.all().aggregate(max_id=Max("pk"))['max_id']
    # while True:
    #     idx = randint(1, max_id)
    #     if Vote.objects.get(pk=idx):
    #         return redirect('votes:detail', idx)
    votes = Vote.objects.all()
    rndvote = choice(votes)
    idx = rndvote.pk
    context = {
        'vote': rndvote
    }
    return redirect('votes:detail', idx)