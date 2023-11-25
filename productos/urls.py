from django.urls import path
from . import views

# productos/
app_name = "productos"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:producto_id>", views.detalle, name="detalle"),
    path("nuevo", views.nuevo, name="nuevo"),
]
