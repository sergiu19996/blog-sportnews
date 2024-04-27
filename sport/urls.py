from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', views.player_list, name='player_list'),
    path('teams/', views.team_list, name='team_list'),
    path('news/', views.news_list, name='news_list'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    # Alte rute URL pentru funcțiile din views.py
]