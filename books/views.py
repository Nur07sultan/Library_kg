from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
import random
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from . import models


class BookListView(ListView):
    model = models.Books
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        genre = self.request.GET.get('genre', '').strip()
        if q:
            qs = qs.filter(title__icontains=q)
        if genre:
            qs = qs.filter(genres__name__iexact=genre)
        return qs.distinct()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['genres'] = models.Genre.objects.order_by('name').all()
        ctx['q'] = self.request.GET.get('q', '').strip()
        ctx['selected_genre'] = self.request.GET.get('genre', '').strip()
        return ctx


book_list_view = BookListView.as_view()


class BookDetailView(DetailView):
    model = models.Books
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        book = self.object
        ctx['reviews'] = book.reviews.all()
        ctx['episodes'] = book.episodes.all()
        episode_id = self.kwargs.get('episode_id')
        if episode_id:
            ctx['current_episode'] = get_object_or_404(models.Episode, id=episode_id, book=book)
        else:
            ctx['current_episode'] = ctx['episodes'].first() if ctx['episodes'].exists() else None
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'text' in request.POST:
            rating = int(request.POST.get('rating', 1))
            text = request.POST.get('text', '')
            if text:
                models.Review.objects.create(book=self.object, rating=rating, text=text)
        return redirect(reverse('books:book_detail', kwargs={'id': self.object.id}))


book_detail_view = BookDetailView.as_view()


class CurrentTimeView(View):
    def get(self, request):
        now = timezone.localtime(timezone.now())
        return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")


current_time = CurrentTimeView.as_view()


class RandomNumberView(View):
    def get(self, request):
        number = random.randint(1, 100)
        return HttpResponse(f"Случайное число: {number}")


random_number = RandomNumberView.as_view()


class AboutMeView(View):
    def get(self, request):
        return HttpResponse(
            "Меня зовут Нурсултан, мне 17 лет. Я учусь в GEEKS 4 месяц на Backend разработке.\n"
            "Так же занимаюсь боксом "
        )


about_me = AboutMeView.as_view()
