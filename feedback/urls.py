from django.urls import path
from .views import CustomerSignUpAPIView, CustomerLoginAPIView

urlpatterns = [
    path('signup/', CustomerSignUpAPIView.as_view(), name='customer-signup'),
    path('login/', CustomerLoginAPIView.as_view(), name='customer-login'),
]
