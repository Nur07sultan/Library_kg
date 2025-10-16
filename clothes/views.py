from django.shortcuts import render, get_object_or_404
from .models import Clothes, Category

def all_clothes(request):
    items = Clothes.objects.all()
    return render(request, 'clothes/all.html', {'items': items})

def men_clothes(request):
    category = get_object_or_404(Category, name="Одежда мужская")
    items = Clothes.objects.filter(categories=category)
    return render(request, 'clothes/men.html', {'items': items})

def women_clothes(request):
    category = get_object_or_404(Category, name="Одежда женская")
    items = Clothes.objects.filter(categories=category)
    return render(request, 'clothes/women.html', {'items': items})

def kids_clothes(request):
    category = get_object_or_404(Category, name="Детская одежда")
    items = Clothes.objects.filter(categories=category)
    return render(request, 'clothes/kids.html', {'items': items})

def search_clothes(request):
    query = request.GET.get('q', '')
    items = Clothes.objects.filter(title__icontains=query) if query else Clothes.objects.none()
    return render(request, 'clothes/search.html', {'items': items, 'query': query})

def item_detail(request, item_id):
    item = get_object_or_404(Clothes, id=item_id)
    return render(request, 'clothes/detail.html', {'item': item})






