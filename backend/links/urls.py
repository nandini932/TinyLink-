from django.urls import path
from . import views

urlpatterns = [
    path('healthz/', views.healthz, name='healthz'),
    path('links/', views.links_view, name='links'),
    path('links/<str:code>/', views.link_detail_view, name='link_detail'),
]
