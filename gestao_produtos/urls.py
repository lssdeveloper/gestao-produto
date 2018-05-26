from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from produtos import urls as produtos_urls
from home import urls as home_urls

urlpatterns = [
    path('', include(home_urls)),
    path('login/', auth_views.login, name='login'),
    path('produtos/', include(produtos_urls)),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
