import requests
import urls
import allure

class MethodsCreatingOrder:

    @allure.step("Создать заказ")
    def create_order(self, payload):
            response = requests.post(f"{urls.BASE_URL}/orders", json=payload)
            return response

