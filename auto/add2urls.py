from django.urls import path
from . import views

urlpatterns = [
    path('fetch_sales_report/', views.fetch_sales_report, name='fetch_sales_report'),
    path('fetch_ongoing_shipments/', views.fetch_ongoing_shipments, name='fetch_ongoing_shipments'),
]
