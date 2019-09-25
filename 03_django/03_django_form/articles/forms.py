from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget = forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='제목',
#         widget = forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#     )

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        max_length=10,
        widget = forms.TextInput(
            attrs = {
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Article
        # fields = ('title', 'content', )
        # exclude = ('title', )
        fields = '__all__'

        # widgets = {
        #     'title': forms.TextInput(attrs = {
        #         'class': 'my-title'
        #     })
        # }