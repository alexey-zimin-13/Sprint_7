import requests
import random
import string
import urls
import allure

class MethodsCreatingOrder:

    @allure.step("Сгенерировать данные заказа")
    def generate_order_data(self, color=None):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        first_name = generate_random_string(8)
        last_name = generate_random_string(8)
        address = f"{generate_random_string(6)}, {random.randint(1, 100)}"
        metro_station = random.randint(1, 10)
        phone = f"+7 {random.randint(100, 999)} {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}"
        rent_time = random.randint(1, 14)
        delivery_date = f"{random.randint(2010, 2030)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        comment = f"Комментарий от {first_name} {last_name}"

        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }

        if color is not None:
            payload["color"] = color

        return payload

    @allure.step("Создать заказ")
    def create_order(self, payload):

        try:
            response = requests.post(f"{urls.BASE_URL}/orders", json=payload)
            return response
        except requests.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            return None

    @allure.step("Получить track-номер из ответа")
    def get_track_from_response(self, response):
  
        if response.status_code == 201 and "track" in response.json():
            return response.json()["track"]
        return ('Код не получен!')
