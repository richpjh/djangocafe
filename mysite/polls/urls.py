from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('order/<int:question_id>/', views.order_details, name='order_details'),
]
