# wordpress_module_tegromoney_python
A Python module for integrating Tegro Money into your wordpress website

Install the module on the WordPress site where you want to use it. 
You can do this by uploading the .tar.gz file from dist directory to the site's plugins directory and then activating it in the WordPress admin panel.

# Available methods
Route for sending requests: '/tegro-payment'

## POST
-Creates a new payment for order passed into it.

### Example request:
```
url = f"https://www.example.com/tegro-payment"
data = {
  "currency": "RUB",
  "amount": 100,
  "order_id": 1,
  "email": "customer_email@gmail.com",
  "phone": "customer_phone@gmail.com",
  "items": [
          {
            "name": "test item 1",
            "count": 1,
            "price": 600
          },
          {
            "name": "test item 2",
            "count": 1,
            "price": 600
          }
        ]
  }
}
requests.post(url, data)
```

POST-request should contain order data for a new payment: currency, amount, order_id, email, phone, items.
If given data is valid, method will redirect user to Tegro.money payment page

## GET
-Checks payment with order_id passed into it on Tegro.money payment system

GET-request should contain order_id of the target payment.
If given data is valid, method will return "Payment succesful order <your_order_id>" if the payment is completed and "Payment not found <your_order_id>" if the payment is not completed.

### Example request:
```
url = f"https://www.example.com/tegro-payment"
data = {
  "order_id": 1
}
requests.post(url, data)
```




