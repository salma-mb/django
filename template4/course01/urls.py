from django.urls import path
from .views import index, view_form

urlpatterns = [
    path('', index, name="home"),
    path('form/', view_form, name="form"),
    # path('contact/', contact, name="contact"),
]