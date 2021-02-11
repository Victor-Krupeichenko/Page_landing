from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('reviews-add/', ReviewsCreate.as_view(), name='reviews_add')
]
