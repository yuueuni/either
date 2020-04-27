from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import VoteForm, CommentForm
from .models import Vote, Comment


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
    context = {
        'vote': vote
    }
    return render(request, 'votes/detail.html', context)


@require_POST
@login_required
def comment(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commt=False)
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
