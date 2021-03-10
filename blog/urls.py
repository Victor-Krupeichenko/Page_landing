from django.urls import path
from .views import *

urlpatterns = [
    path('', NotesViews.as_view(), name='blog'),
    path('category/<str:slug>/', NotesByCategories.as_view(), name='category'),
    path('vievs-notes/<str:slug>/', ViewsNotes.as_view(), name='views_notes'),
    path('tags-notes/<str:slug>/', NotesTags.as_view(), name='tags_notes'),
    path('search/', Search.as_view(), name='search'),
    path('commit-notes/<int:pk>/', AddComment.as_view(), name='commit_notes'),
    path('delete-messages/<int:pk>/', delete_messages, name='messages_delete'),
    path('notes/create-notes/', CreatedNotes.as_view(), name='created_notes'),
]
