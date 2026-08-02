from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('do-you-love-me/', views.love_query, name='love_query'),  # MAKE SURE THIS IS HERE
    path('memories/', views.memories, name='memories'),
    path('forever-vault/', views.final_vault, name='final_vault'),

]
