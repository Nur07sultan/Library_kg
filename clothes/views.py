from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Clothes, Category


class AllClothesView(ListView):
    model = Clothes
    template_name = 'clothes/all.html'
    context_object_name = 'items'


all_clothes = AllClothesView.as_view()


class CategoryClothesView(ListView):
    model = Clothes
    template_name = None  # to be set per-instance
    context_object_name = 'items'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        category = get_object_or_404(Category, name=category_name)
        return Clothes.objects.filter(categories=category)

    def get_template_names(self):
        # map category names to templates
        mapping = {
            'Одежда мужская': 'clothes/men.html',
            'Одежда женская': 'clothes/women.html',
            'Детская одежда': 'clothes/kids.html',
        }
        return [mapping.get(self.kwargs.get('category_name'), 'clothes/all.html')]


def men_clothes(request):
    view = CategoryClothesView.as_view()
    return view(request, category_name='Одежда мужская')


def women_clothes(request):
    view = CategoryClothesView.as_view()
    return view(request, category_name='Одежда женская')


def kids_clothes(request):
    view = CategoryClothesView.as_view()
    return view(request, category_name='Детская одежда')


class SearchClothesView(ListView):
    model = Clothes
    template_name = 'clothes/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Clothes.objects.filter(title__icontains=query) if query else Clothes.objects.none()


search_clothes = SearchClothesView.as_view()


class ItemDetailView(DetailView):
    model = Clothes
    template_name = 'clothes/detail.html'
    pk_url_kwarg = 'item_id'
    context_object_name = 'item'


item_detail = ItemDetailView.as_view()






