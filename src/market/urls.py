from django.urls import path

from . import views

urlpatterns = [
    path("api/history/<str:symbol>/", views.stock_history, name="stock_history"),
]
