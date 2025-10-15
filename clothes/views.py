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




from django.http import JsonResponse
from django.core.serializers import serialize

def clothes_ajax(request):
    # category: all / men / women / kids
    category = request.GET.get('category', 'all')
    q = request.GET.get('q', '').strip()

    items = Clothes.objects.all()

    if category == 'men':
        try:
            cat = Category.objects.get(name="Одежда мужская")
            items = items.filter(categories=cat)
        except Category.DoesNotExist:
            items = items.none()
    elif category == 'women':
        try:
            cat = Category.objects.get(name="Одежда женская")
            items = items.filter(categories=cat)
        except Category.DoesNotExist:
            items = items.none()
    elif category == 'kids':
        try:
            cat = Category.objects.get(name="Детская одежда")
            items = items.filter(categories=cat)
        except Category.DoesNotExist:
            items = items.none()

    if q:
        items = items.filter(title__icontains=q)

    data = []
    for it in items:
        data.append({
            'id': it.id,
            'title': it.title,
            'description': it.description or '',
            'price': str(it.price),
            'image': it.image.url if it.image else '',
        })
    return JsonResponse({'items': data})
