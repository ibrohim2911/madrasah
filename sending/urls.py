from django.urls import path
from .views import registerview, doneview
urlpatterns = [
    path('', registerview.as_view(), name='home'),
    path('done/', doneview.as_view(), name='signup')
]