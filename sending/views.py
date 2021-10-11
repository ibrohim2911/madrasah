from django.views.generic import CreateView
from .signup import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class registerview(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/index.html'
    success_url = reverse_lazy('signup')
class doneview(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

