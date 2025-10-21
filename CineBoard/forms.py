from django import forms
from .models import Movie
from .models import MovieComment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'release_date', 'rating', 'tags', 'poster']
        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'}),
            'genres': forms.SelectMultiple(attrs={'size':6}),
            'tags': forms.SelectMultiple(attrs={'size':6}),
        }


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min':1, 'max':5}),
            'text': forms.Textarea(attrs={'rows':3}),
        }
