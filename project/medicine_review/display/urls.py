from django.urls import path
from django.conf.urls import url
from . import views
from .views import add_category, blog, med_edit, post_details,add_post,edit_post,delete_post,category,profile,likes,add_comment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.home, name='home'),
    path('profile',profile.as_view(), name='profile'),
    path('main',views.main,name='main'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('feedback',views.feedback,name='feedback'),
    path('check',views.check,name='check'),
    path('check/<int:id>', views.med_edit, name='med_edit'),
    path('check/<int:id>/comment', add_comment.as_view(), name='add_comment'),
    path('blog',blog.as_view(),name="blog"),
    path('post_details/<int:pk>',post_details.as_view(),name="post_details"),
    path('add_post',add_post.as_view(),name="add_post"),
    path('add_category',add_category.as_view(),name="add_category"),
    path('edit_post/<int:pk>',edit_post.as_view(),name="edit_post"),
    path('delete_post/<int:pk>',delete_post.as_view(),name="delete_post"),
    path('category/<str:cat>/',category,name='category'),
    path('likes/<int:pk>',likes, name='likes')
    ]
urlpatterns += staticfiles_urlpatterns()