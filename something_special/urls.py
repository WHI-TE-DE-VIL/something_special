from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Home import views  # <-- MASTER IMPORT FIX

urlpatterns = [
    path('admin/', admin.site.urls),

    # MASTER ROUTING ALIASES: Built straight into the root core server engine
    path('', views.home, name='home'),
    path('do-you-love-me/', views.love_query, name='love_query_old'),
    path('love-query/', views.love_query, name='love_query'),
    path('beginning/', views.beginning, name='beginning'),
    path('forever-vault/', views.forever_vault, name='forever_vault'),
    path('memories/', views.memories, name='memories'),
    path('ending-page/', views.ending_page, name='ending_page'),

    # Fallback include statement
    path('', include('Home.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
