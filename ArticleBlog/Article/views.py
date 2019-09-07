from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response

from  Article.models import *
from django.core.paginator import Paginator

def set_page(page_list,page):
    """
    page_list  # 页码范围
    page #页码
    想要当前页码的前两页和后两页
    """
    if page - 3 < 0:
        start = 0
    else:
        start = page - 3
    if page+2 > 49:
        end = 49
    else:
        end = page+2
    return list(page_list[start:end])


def index(request):
    new_article=Article.objects.order_by('-public_time')[:6]
    recom_article=Article.objects.filter(recommend=1).order_by('-public_time')[:7]
    click_article=Article.objects.order_by('-click')[:12]
    return render_to_response('index.html',locals())

def about(request,id):
    article=Article.objects.get(id=int(id))
    return render_to_response('about.html',locals())

def newlist(request,types,p):
    p=int(p)
    page_size=6
    aa=Article.objects.last()
    article=ArticleType.objects.get(label=types).article_set.order_by('-public_time')
    # article_list=Article.objects.all()
    article_list=Paginator(article,page_size)  #进行分页
    page_article=article_list.page(p)          #返回对应页的数据
    page_range=set_page(article_list.page_range,p)
    return render_to_response('newlist.html',locals())

def listpic(request):
    return render_to_response('listpic.html',{})

