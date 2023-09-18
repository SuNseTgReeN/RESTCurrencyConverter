from django.urls import path

from CurrencyConverter.views import CurrencyConverterView

app_name = 'CurrencyConverter'

urlpatterns = [
    path('rates/', CurrencyConverterView.as_view(), name='currency_converter'),
]
