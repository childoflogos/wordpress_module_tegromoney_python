from hashlib import sha256
from flask import Flask, request, redirect
import hmac
import json
import time
import requests
import config


app = Flask(__name__)


@app.route('/tegro-payment', methods=['POST', 'GET'])
def tegro_payment():
    order = request.json

    # Создание платежа через Tegro и редирект на страницу оплаты
    if request.method == 'POST':
        try:
            url = 'https://tegro.money/api/createOrder/'
            data = {
                "shop_id": config.shop_id,
                "nonce": time.time(),
                "currency": f"{order['currency']}",
                "amount": f"{order['amount']}",
                "order_id": order['order_id'],
                "payment_system": 1,
                "fields": {
                    "email": f"{order['email']}",
                    "phone": f"{order['phone']}"
                },
                "receipt": order['items']
            }
            body = json.dumps(data)
            sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()
            headers = {
                "Authorization": f"Bearer {sign}",
                "Content-Type": "application/json"
            }
            response = requests.post(url=url, headers=headers, data=data)
            if response:
                payment_url = response.json()['data']['url']
                return redirect(payment_url)
            else:
                return f'Error. No response from Tegro. Error code: {response.status_code}'
        except:
            return f'Error. Impossible to fulfill the request.'

    #Получение данных о платеже
    else:
        try:
            url = 'https://tegro.money/api/order/'

            params = {
                "shop_id": config.shop_id,
                "nonce": time.time(),
                "order_id": order['order_id'],
                "payment_id": "test order"
            }

            body = json.dumps(params)
            sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

            headers = {
                "Authorization": f"Bearer {sign}",
                "Content-Type": "application/json"
            }

            response = requests.post(url=url, headers=headers, params=params)
            order = response.json()
            if order['type'] == "success":
                return f'Payment succesful order {order["order_id"]}'
            else:
                return f'Payment not found {order["order_id"]}'
        except:
            return f'Error. Impossible to fulfill the request.'


if __name__ == '__main__':
    app.run()
