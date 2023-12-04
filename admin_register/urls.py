from django.urls import path
from admin_register import views

urlpatterns = [
    path('', views.register_view),
]
