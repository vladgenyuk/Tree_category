from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>/', views.details, name='categories'),
    path('category/<str:category>/<int:cat_id>/', views.products, name='products'),
    path('create_1', views.create_products, name='create_10'),
    path('about', views.about, name='about'),
]