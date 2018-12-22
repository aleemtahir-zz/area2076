from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('area2076.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    # path('', RedirectView.as_view(url='', permanent=False)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
