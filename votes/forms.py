from django import forms
from .models import Vote, Comment


class VoteForm(forms.ModelForm):
    issue_r = forms.CharField(
        label='Option RED',
        widget=forms.TextInput(attrs={'placeholder': 'option content'}),
    )
    issue_b = forms.CharField(
        label='Option BLUE',
        widget=forms.TextInput(attrs={'placeholder': 'option content'}),
    )

    class Meta:
        model = Vote
        fields = ['title', 'issue_r', 'issue_b']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pick', 'content']
