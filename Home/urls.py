from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('love-query/', views.love_query, name='love_query'),  # MATCHED: Fixes the Homepage button error!
    path('beginning/', views.beginning, name='beginning'),
    path('forever-vault/', views.forever_vault, name='forever_vault'), # SYNCHRONIZED
    path('memories/', views.memories, name='memories'),
    path('ending-page/', views.ending_page, name='ending_page'), # SYNCHRONIZED
]
