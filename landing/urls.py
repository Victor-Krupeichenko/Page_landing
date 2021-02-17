from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('read-more-single/<str:slug>/', InspireViews.as_view(), name='single_inspire'),
    path('reviews-add/', ReviewsCreate.as_view(), name='reviews_add'),
    path('reviews-all/', ReviewsAll.as_view(), name='reviews_all')
]
