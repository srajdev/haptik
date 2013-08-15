from django import forms
from api.models.default import Business, Location, Category
from api import const


class LocationModelChoice(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.location


class CategoryModelChoice(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.category

class BusinessForm(forms.ModelForm):
    category = CategoryModelChoice(queryset = Category.objects.all(), widget=forms.Select())
    location = LocationModelChoice(queryset=Location.objects.all(), widget=forms.Select())
    class Meta:
        category = CategoryModelChoice(queryset = Category.objects.all(), widget=forms.Select())
        location = LocationModelChoice(queryset=Location.objects.all(), widget=forms.Select())
        model = Business
        fields = ('name', 'xmpp_handle', 'email', 'location', 'website', 'facebook', 'twitter', 'category')