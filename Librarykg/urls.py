from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('books.urls', namespace='books')),
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls', namespace='basket')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('captcha/', include('captcha.urls')),  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)