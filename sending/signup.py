from django.contrib.auth.forms import UserCreationForm
from .models import signupUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = signupUser
        fields = ('username', 'number')