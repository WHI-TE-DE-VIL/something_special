from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),  # This handles passing all sub-paths down to your app!
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
