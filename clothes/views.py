from django.shortcuts import render
from .models import Clothes, Category

def men_clothes(request):
    category = Category.objects.get(name="Одежда мужская")
    items = Clothes.objects.filter(categories=category)
    return render(request, 'clothes/men.html', {'items': items})

def women_clothes(request):
    category = Category.objects.get(name="Одежда женская")
    items = Clothes.objects.filter(categories=category)
    return render(request, 'clothes/women.html', {'items': items})

def kids_clothes(request):
    category = Category.objects.get(name="Детская одежда")
    items = Clothes.objects.filter(categories=category)
    return render(request, 'clothes/kids.html', {'items': items})

def search_clothes(request):
    query = request.GET.get('q')
    items = Clothes.objects.filter(title__icontains=query) if query else []
    return render(request, 'clothes/search.html', {'items': items, 'query': query})

def all_clothes(request):
    items = Clothes.objects.all()
    return render(request, 'clothes/all.html', {'items': items})


