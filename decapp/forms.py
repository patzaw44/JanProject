from django.forms import ModelForm
from .models import Auto

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ["make", "model"]