from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index),
    path('book_query/', views.book_query),
    path('deal_query/', views.deal_query),
    path('member_query/', views.mermber_query),
    path('inout_query/', views.inout_query),
]
