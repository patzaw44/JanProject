from django.forms import ModelForm
from .models import Car

class AutoForm(ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model"]
