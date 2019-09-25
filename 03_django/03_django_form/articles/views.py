from IPython import embed

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

        
# def create(request):
#     if request.method == 'POST':
#       title = request.POST.get('title')
#       content = request.POST.get('content')
#       artice = Article(title=title, content=content)
#       artice.save()
#       return redirect(article)
#     else:
#         return render(request, 'articles/create.html')


# def detail(request, article_pk):
#     try:
#         article = Article.objects.get(pk=article_pk)
#     except:
#         raise Http404('No article mathes the given query.')
#     context = {'article': article, }
#     return render(request, 'articles/detail.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article, }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            article = form.save()
            return redirect(article)
    else:
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        # form = ArticleForm(initial=article.__dict__)
        form = ArticleForm(instance=article)
        
    context = {'form': form, 'article': article} 
    return render(request, 'articles/form.html', context)