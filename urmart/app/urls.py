
from django.urls import path

from app import views


urlpatterns = [
    path('view', views.order_view, name='view-order'),
]
