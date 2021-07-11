from django.shortcuts import render, get_object_or_404,redirect
from.models import Story,Category
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import messages
import random


# Create your views here.



def story_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    story = Story.objects.all()
    print("leg of all story ",len(story))
    paginator=Paginator(story,4)
    page=request.GET.get('page')
    try:
        story=paginator.page(page)
    except PageNotAnInteger:
        story=paginator.page(1)
    except EmptyPage:
        story=paginator.page(paginator.num_pages)
    if category_slug:
        story=Story.objects.all()
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
        paginator = Paginator(story,2)
        page = request.GET.get('page')
        try:
            story = paginator.page(page)
        except PageNotAnInteger:
            story = paginator.page(1)
        except EmptyPage:
            story = paginator.page(paginator.num_pages)
    all_story = list(Story.objects.all())
    recent_story = random.sample(all_story,2)
    return render(request,"story_list.html",{'categories':categories,'category':category,'story':story,'page':page,'recent_story':recent_story,})


def story_detail(request,id):
    story=get_object_or_404(Story,id=id)
    all_story = list(Story.objects.exclude(id=id))
    like_story = random.sample(all_story,2)

    return render(request,'story_detail.html',{'story':story,'like_story':like_story,})


def search_story(request):
    query=None
    results=[]
    if request.method =='GET':
        query = request.GET.get("search")
        results = Story.objects.filter(Q(title__icontains=query)| Q(body__icontains=query))
        return render(request,'search.html',{'query':query,'results':results})

