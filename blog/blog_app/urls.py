from . import views
from django.urls import path

urlpatterns = [
    path('index',views.index,name="index"),
    path('home',views.home,name="home"),
    path('register',views.registerUser,name="register"),
    path('login',views.loginUser,name="login"),

    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]