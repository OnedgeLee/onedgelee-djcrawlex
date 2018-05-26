from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.

def show_list(request):
    latest_article_list = Article.objects.order_by('article_crawldate')[:10]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'best_comment/list.html', context)