from django.urls import path
from .views import NotesViews, NotesByCategories, ViewsNotes

urlpatterns = [
    path('', NotesViews.as_view(), name='blog'),
    path('category/<str:slug>/', NotesByCategories.as_view(), name='category'),
    path('vievs-notes/<str:slug>/', ViewsNotes.as_view(), name='views_notes'),
]
