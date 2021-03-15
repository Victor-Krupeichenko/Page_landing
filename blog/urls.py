from django.urls import path
from .views import *

urlpatterns = [
    path('', NotesViews.as_view(), name='blog'),
    path('category/<str:slug>/', NotesByCategories.as_view(), name='category'),
    path('detail-notes/<str:slug>/', DetailNote.as_view(), name='detail_notes'),
    path('tags-notes/<str:slug>/', NotesTags.as_view(), name='tags_notes'),
    path('search/', Search.as_view(), name='search'),
    path('commit-notes/<int:pk>/', AddComment.as_view(), name='commit_notes'),
    path('delete-messages/<int:pk>/', delete_messages, name='messages_delete'),
    path('notes/create-notes/', CreatedNotes.as_view(), name='created_notes'),
    path('notes-delete/<slug:slug>/', delete_notes, name='delete_notes'),
    path('update-notes/<str:slug>/', NotesUpdate.as_view(), name='update_notes'),
    path('update_comment/<int:pk>/', CommentsUpdate.as_view(), name='comment_update'),
    path('register-user/', RegisterUserView.as_view(), name='register_user'),
    path('login-user/', UserLogin.as_view(), name='login_user'),
    path('logout-user/', UserLogout.as_view(), name='logout_user'),
]
