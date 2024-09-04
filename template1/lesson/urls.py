from django.urls import path
from  .views import index, view

urlpatterns = [
    path('', index, name="home"),
    path('form/', view, name="form"),
    # path('contact/', contact, name="contact"),
]