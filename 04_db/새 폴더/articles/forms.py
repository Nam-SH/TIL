from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        )
    )
    content = forms.CharField(
        label='내용',
    )
    
    class Meta:
        model = Article
        field = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fidld = ('content',)