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
    path('member_log/', views.member_log),

    path('deal_query/', views.deal_query),
    path('deal_manage/', views.deal_manage),
    path('deal_new', views.deal_new),

    path('inout_query/', views.inout_query),
    path('inout_manage/', views.inout_manage),
    path('inout_new', views.inout_new),
    path('inout_modify/', views.inout_modify),
    path('inout_log/', views.inout_log),
]
