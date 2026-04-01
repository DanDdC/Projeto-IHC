from django.contrib import admin  
from django.urls import path
from gekkoteca import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.auth_view, name='auth'),
    path('home/', views.home_view, name='home'),
    path('pesquisa/', views.search_view, name='search'),
    path('livro/<int:livro_id>/', views.livro_view, name='livro_detail'),
    path('carrinho/add/<int:livro_id>/', views.add_carrinho, name='add_carrinho'), # NOVA
    path('carrinho/', views.carrinho_view, name='carrinho_view'), # NOVA
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)