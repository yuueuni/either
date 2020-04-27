from django import forms
from .models import Vote, Comment


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
