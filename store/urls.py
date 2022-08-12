from django.urls import path
from . import views
urlpatterns=[
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('',views.store,name='store'),
    path('update_item/' , views.updateitem,name="update_item")
    ]