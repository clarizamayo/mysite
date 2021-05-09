from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Adoption

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ['email', 'message']