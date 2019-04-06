from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from article.models import Article

# Create your views here.

def article_detail(request, article_id):    
    # context = {}
    # try:
    #     # article = Article.objects.get(id=article_id)
    #     article = Article.objects.get(pk=article_id)
    #     context['article'] = article
    #     return render_to_response('article_detail.html', context=context)
    # except Article.DoesNotExist:
    #     raise Http404("not exist")
        # return HttpResponse("不存在")
    # return HttpResponse('article_title: %s' %article.title)
    
    # 优化上面404
    context = {}
    article = get_object_or_404(Article, pk=article_id)
    context['article'] = article
    return render_to_response('article_detail.html', context=context)

def article_list(request):
    artilces = Article.objects.filter(is_deleted=False)
    context = {}
    context['articles'] = artilces
    return render_to_response('article_list.html', context=context)
    