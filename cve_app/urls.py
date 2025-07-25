from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cves/', views.cve_list, name='cve_list'),
    path('cves/<str:cve_id>/', views.cve_detail, name='cve_detail'),
]
