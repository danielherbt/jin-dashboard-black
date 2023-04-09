"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularYAMLAPIView
from rest_framework import permissions
from django.urls import path, include, re_path


urlpatterns = [
    path("", include('admin_black.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # # Open API 자체를 조회 : json, yaml, 
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("docs/yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
    # Open API Document UI로 조회: Swagger, Redoc
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui",),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc",),
    # Api routes
    path('api/administracion/', include('api.manage.urls')),
    path('api/escuelacobros/', include('api.schoolfees.urls')),
    path('api/ventas/', include('api.sales.urls')),
    path('api/documentos/', include('api.docs.urls')),
    # Leave `Home.Urls` as last the last line
    path("", include("home.urls")),
    path("", include("mobile.urls"))
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns +=[
#    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,})
#] 