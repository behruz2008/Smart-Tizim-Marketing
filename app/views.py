from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView
from .models import *


class XususiyatViews(ListView):
    model = Xususiyat
    template_name = "xususiyat.html"
    context_object_name = "Xususiyat"


def index(request):
    jamoa = Jamoa.objects.all()
    statistika = Statistika.objects.all()
    tarif = Tarif.objects.all()
    xizmat = Xizmat.objects.all()
    xususiyat = Xususiyat.objects.all()
    blog = Blog.objects.all()
    blog_post = Blog.objects.all()
    link = Link.objects.all()
    malumot = Malumot.objects.all()
    contex = {
        'Jamoa': jamoa,
        'Xususiyat': xususiyat,
        'Statistika': statistika,
        'Malumot': malumot,
        'Tarif': tarif,
        'Xizmat': xizmat,
        'Link': link,
        'Blog': blog,
        'Blog_post': blog_post
    }
    return render(request, ['index.html', 'xususiyat.html'], contex)


def blog(requests):
    return render(requests, 'blog.html', {"blog": Blog.objects.all()})


def post_detail(request, id):
    blog = Blog.objects.get(id=id)
    blog.kurishlar = blog.kurishlar + 1
    blog.save()
    return render(request, 'blog-post.html', {"posts": blog})
