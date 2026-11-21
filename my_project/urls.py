from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # INCLUIR LAS RUTAS HIJAS (aquí está /programas/crear/)
    path('', include("myapp.urls")),
    # La raíz del sitio lleva directo al formulario
    path('', RedirectView.as_view(pattern_name="crear_programa", permanent=False)),
]
