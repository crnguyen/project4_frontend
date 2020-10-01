from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    location = forms.CharField()

class RestaurantForm(forms.Form):
    restaurant = forms.CharField()

class FavoriteForm(forms.Form):
    favorites = forms.CharField()