from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
    

def delete(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    article.delete()
    return redirect('articles:index')


@require_POST
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 객체를 Create 하지만, db 에 레코드는 작성하지 않는다.
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)