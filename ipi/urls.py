from django.urls import path
from .views import IPAddressView

urlpatterns = [
    path('get-country/', IPAddressView.as_view(), name='get_country'),
]
