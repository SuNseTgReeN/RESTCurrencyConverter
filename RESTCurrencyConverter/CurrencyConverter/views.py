import os

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializers import CurrencyConversionSerializer


class CurrencyConverterView(APIView):
    permission_classes = [AllowAny]
    """
    API View для конвертации валюты.

    Параметры запроса:
    - base_currency (обязательный): код валюты, из которой производится конвертация.
    - currencies (обязательный): код валюты, в которую производится конвертация.
    - many (опциональный): значение, которое необходимо конвертировать. По умолчанию 0.
    - apikey (обязательный): ключ API, который можно получить на сайте https://app.currencyapi.com

    Пример запроса:
    GET /api/rates/?base_currency=USD&currencies=RUB&value=1&apikey=API_KEY

    Пример ответа:
    {
    "base_currency": "USD",
    "currencies": "RUB",
    "many": 5.0,
    "data": 483.517204673
    }
    """
    def get(self, request):
        serializer = CurrencyConversionSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        frome = serializer.validated_data['base_currency']
        to = serializer.validated_data['currencies']
        key = os.getenv("API_KEY")
        many = serializer.validated_data['many']
        url = f"https://api.currencyapi.com/v3/latest?&base_currency={frome}&currencies={to}&apikey={key}"
        response = requests.get(url)
        data_json = response.json()
        rate = data_json['data'][to]['value']
        data = many * rate

        serializer.validated_data['data'] = data
        return Response(serializer.validated_data)
