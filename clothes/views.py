from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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
    items = Clothes.objects.filter(title__icontains=query) if query else []
    return render(request, 'clothes/search.html', {'items': items, 'query': query})

def clothes_ajax(request):
    category = request.GET.get('category', 'all')
    q = request.GET.get('q', '').strip()

    items = Clothes.objects.all()
    if category != 'all':
        cat_map = {
            'men': "Одежда мужская",
            'women': "Одежда женская",
            'kids': "Детская одежда"
        }
        try:
            cat = Category.objects.get(name=cat_map[category])
            items = items.filter(categories=cat)
        except Category.DoesNotExist:
            items = items.none()

    if q:
        items = items.filter(title__icontains=q)

    data = [{
        'id': it.id,
        'title': it.title,
        'description': it.description or '',
        'price': str(it.price),
        'image': it.image.url if it.image else '',
    } for it in items]

    return JsonResponse({'items': data})






