from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('profile/',views.profile,name='profile'),
    path('logout/',auth_view.LogoutView.as_view(template_name='store/logout.html'),name='logout'),
    path('',views.store,name='store'),
    path('update_item/' , views.updateitem,name="update_item"),
    path('login/',auth_view.LoginView.as_view(template_name='store/login.html'),name='login'),
    path('register/',views.register,name='register'),
    
    ]