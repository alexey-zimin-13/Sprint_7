import random
import allure
from helpers.data_generation import DataGeneration

class MethodsGenerationOrderData:

    @allure.step("Сгенерировать данные заказа")
    def generate_order_data(self, color=None):

        generate_string = DataGeneration()

        first_name = generate_string.generate_random_string(8)
        last_name = generate_string.generate_random_string(8)
        address = f"{generate_string.generate_random_string(6)}, {random.randint(1, 100)}"
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