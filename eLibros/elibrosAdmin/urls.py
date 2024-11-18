from django.conf.urls.static import static

from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("djangoadmin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("elibrosLoja.urls.HomeUrls")),
    path("acervo/", include("elibrosLoja.urls.LivroUrls")),
    path("cliente/", include("elibrosLoja.urls.ClienteUrls")),
    path("carrinho/", include("elibrosLoja.urls.CarrinhoUrls")),
    path("admin/", include("elibrosLoja.urls.AdminUrls")),  
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)