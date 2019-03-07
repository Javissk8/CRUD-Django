from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('business/detail/<int:business_id>', views.detail_business, name='detail_business'),
    path('business/create/', views.create_business, name='create_business'),
    path('business/delete/<int:business_id>', views.delete_business, name='delete_business'),
    path('business/edit/<int:business_id>', views.edit_business, name='edit_business'),
    path('business/create-comment/<int:business_id>', views.create_comment, name='create_comment'),
    path('business/edit-comment/<int:business_id>', views.edit_comment, name='edit_comment'),
    path('business/detail-comment/<int:business_id>', views.detail_comment, name='detail_comment'),
    path('business/create-promo/<int:business_id>', views.create_promo, name='create_promo'),
    path('business/detail-promo/<int:business_id>', views.detail_promo, name='detail_promo'),


]