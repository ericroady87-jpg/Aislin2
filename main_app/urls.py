from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include 
from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name="about"),
    path('ms/', views.ms_index, name='ms-index'),
    path('ms/<int:ms_id>/', views.ms_detail, name='ms-detail'),
    path('ms/create/', views.MsCreate.as_view(), name='ms-create'),
    path('ms/<int:pk>/update/', views.MsUpdate.as_view(), name='ms-update'),
    path('ms/<int:pk>/delete/', views.MsDelete.as_view(), name='ms-delete'),
    path('ms/<int:ms_id>/add-fueling/', views.add_fueling, name='add-fueling'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapon-create'),
    path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapon-detail'),
    path('weapons/', views.WeaponList.as_view(), name='weapon-index'),
    path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapon-update'),
    path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapon-delete'),
    path('ms/<int:ms_id>/associate-weapon/<int:weapon_id>/', views.associate_weapon, name='associate-weapon'),
    path('ms/<int:ms_id>/remove-weapon/<int:weapon_id>/', views.remove_weapon, name='remove-weapon'),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path('', views.Home.as_view(), name='home'),

    path('accounts/signup/', views.signup, name='signup'),

]