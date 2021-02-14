from django.urls import path
from .views import NotesViews, NotesByCategories

urlpatterns =[
    path('', NotesViews.as_view(), name='blog'),
    path('category/<str:slug>/', NotesByCategories.as_view(), name='category' )
]
