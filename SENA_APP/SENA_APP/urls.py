from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('aprendices.urls')),
    path('', include('instructores.urls')),
    path('', include('programas.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Panel de Administración SENA'
admin.site.site_title = 'SENA APP'
admin.site.index_title = 'Gestión de Aprendices'