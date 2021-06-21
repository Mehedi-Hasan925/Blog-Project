from django import forms
from blog_app import models


class LikeForm(forms.ModelForm):
    class Meta:
        model = models.like
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ('comment_content',)
        