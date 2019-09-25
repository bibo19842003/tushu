from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index),

    path('book_query/', views.book_query),

    path('member_query/', views.member_query),
    path('member_manage/', views.member_manage),
    path('member_new', views.member_new),
    path('member_modify/', views.member_modify),
    path('member_log', views.member_log),

    path('deal_query/', views.deal_query),

    path('inout_query/', views.inout_query),
]
