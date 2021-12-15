from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("shop/", views.shop, name="shop"),
path("order/", views.order, name="order"),
path("homedb/", views.homedb, name="homedb"),
path("create/", views.create, name="create"),
path("delete/", views.delete, name="delete"),
path("views/", views.views, name="view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)