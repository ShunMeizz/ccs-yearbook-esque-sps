from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_home, name='blog_home'),
    path('blog/delete/<int:user_id>/', views.delete_post, name='delete_post'),
    path('blog/post/<int:post_id>',views.view_post,name="view_post"),
    # path('blog/edit/<int:post_id>',views.edit_post,name="edit_post"),
    path('blog_search/', views.blog_search, name='blog_search'),
    path('blog/test', views.intermediary, name='intermediary'),
    path('blog/my_blogs=<int:user_id>', views.my_post, name='pending'),
]