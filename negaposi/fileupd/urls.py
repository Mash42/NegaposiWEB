from django.conf.urls import url
from fileupd import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
    url('$^', views.post_message),
    url('post_list/', views.PostListView.as_view()),
]
