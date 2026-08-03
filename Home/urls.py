from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # THE DOUBLE-ROUTE ALIAS TRICK: Catches both path requests safely!
    path('do-you-love-me/', views.love_query, name='love_query_old'),
    path('love-query/', views.love_query, name='love_query'),

    path('beginning/', views.beginning, name='beginning'),
    path('forever-vault/', views.forever_vault, name='forever_vault'),
    path('memories/', views.memories, name='memories'),
    path('ending-page/', views.ending_page, name='ending_page'),
]
