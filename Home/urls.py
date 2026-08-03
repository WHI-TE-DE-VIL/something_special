from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('do-you-love-me/', views.love_query, name='love_query'),  # MAKE SURE THIS IS HERE
    path('beginning/', views.beginning, name='beginning'),
    path('forever-vault/', views.forever_vault, name='final_vault'),
    path('memories/', views.memories, name='memories'),
    path('ending-page/', views.ending_page, name='ending-page'),

]
