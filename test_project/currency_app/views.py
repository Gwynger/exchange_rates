from django.shortcuts import render
import requests
import time
from .models import Currency
from dotenv import dotenv_values

ENV = dotenv_values('../.env')


def get_current_usd(request):
    api_key = ENV['API_KEY']
    base_currency = 'USD'
    target_currency = 'RUB'
    api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        conversion_rates = data['conversion_rates']
        usd_to_rub_rate = conversion_rates.get(target_currency)
        Currency.objects.create(usd_to_rub=usd_to_rub_rate)
        last_10_rates = Currency.objects.order_by('-timestamp')[:10]
        time.sleep(10)
        return render(request, 'currency_template.html', {'usd_to_rub_rate': usd_to_rub_rate, 'last_10_rates': last_10_rates})

    except requests.exceptions.RequestException as e:
        return render(request, 'error_template.html', {'error_message': f'Ошибка запроса к API: {e}'})

    except KeyError:
        return render(request, 'error_template.html', {'error_message': 'Неверная структура данных от API'})
