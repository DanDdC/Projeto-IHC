from django.urls import path
from gekkoteca import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.auth_view, name='auth'),
    path('home/', views.home_view, name='home'),
]

# Adicione isso no final do arquivo:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)