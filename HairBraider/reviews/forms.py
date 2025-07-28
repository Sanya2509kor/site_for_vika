from django import forms
from reviews.models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment']