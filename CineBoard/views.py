from django.views.generic import TemplateView, ListView, DetailView
from . import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from .forms import MovieForm
from accounts.forms import CustomUserCreationForm, SimpleCustomUserCreationForm, MinimalUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models import Avg
from .forms import MovieCommentForm

class IndexView(TemplateView):
    template_name = 'cineboard/index.html'

class ChannelListView(ListView):
    model = models.Channel
    template_name = 'cineboard/channels.html'
    context_object_name = 'channels'

class ItemDetailView(DetailView):
    model = models.CineItem
    template_name = 'cineboard/item_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'item'


class MovieListView(ListView):
    model = models.Movie
    template_name = 'cineboard/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        genre = self.request.GET.get('genre', '').strip()
        tag = self.request.GET.get('tag', '').strip()
        sort = self.request.GET.get('sort', '').strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if genre:
            qs = qs.filter(genres__name__iexact=genre)
        if tag:
            qs = qs.filter(tags__name__iexact=tag)
        qs = qs.distinct()
        if sort == 'rating':
            # annotate average rating from comments
            qs = qs.annotate(avg_rating=Avg('comments__rating')).order_by('-avg_rating')
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['genres'] = models.Genre.objects.order_by('name').all()
        ctx['tags'] = models.Tag.objects.order_by('name').all()
        ctx['selected_genre'] = self.request.GET.get('genre', '').strip()
        ctx['selected_tag'] = self.request.GET.get('tag', '').strip()
        ctx['q'] = self.request.GET.get('q', '').strip()
        return ctx

    def dispatch(self, request, *args, **kwargs):
        # If user not authenticated, redirect to registration page first
        if not request.user.is_authenticated:
            # preserve next to return after login
            register_url = reverse_lazy('cineboard:register')
            return redirect(f"{register_url}?next={request.path}")
        return super().dispatch(request, *args, **kwargs)


class MovieDetailView(DetailView):
    model = models.Movie
    template_name = 'cineboard/movie_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comments'] = self.object.comments.select_related('user').all()
        ctx['comment_form'] = MovieCommentForm()
        return ctx

    def post(self, request, *args, **kwargs):
        # Handle comment submission
        if not request.user.is_authenticated:
            return redirect('cineboard:login')
        self.object = self.get_object()
        form = MovieCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = self.object
            comment.save()
        return redirect('cineboard:movie_detail', id=self.object.id)


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = models.Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('cineboard:movie_detail', args=[self.object.id])


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse('cineboard:movie_detail', args=[self.object.id])


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Movie
    template_name = 'cineboard/movie_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('cineboard:movie_list')


class RegisterView(FormView):
    # Use a fullscreen registration template for the CineBoard flow
    template_name = 'cineboard/register_fullscreen.html'
    # Use the minimal form (username + password) for a super-simple registration
    form_class = MinimalUserCreationForm

    def form_valid(self, form):
        # Save user but do not auto-login. Redirect to login with next param.
        form.save()
        # Determine where to return after login: prefer provided next, otherwise movie list
        next_url = self.request.GET.get('next') or self.request.POST.get('next') or reverse('cineboard:movie_list')
        login_url = reverse('cineboard:login')
        return redirect(f"{login_url}?next={next_url}")


class LoginView(FormView):
    # fullscreen login for CineBoard flow
    template_name = 'cineboard/login_fullscreen.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('cineboard:movie_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        # redirect to next if provided
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('cineboard:movie_list')
