from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.comment, name='comment'),
    path('comment/create_profile_comment/<int:profile_id>', views.create_profile_comment, name='create_profile_comment'),
    path('comment/create_blog_comment/<int:blog_id>', views.create_blog_comment, name='create_blog_comment'),
    path('comment/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('comment/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]