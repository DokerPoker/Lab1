from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('^post/new/$', views.post_new, name='post_new'),
    path('^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
]
