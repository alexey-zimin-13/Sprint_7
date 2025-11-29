import requests
import urls
import allure

class MethodsLoginCourier:

    @allure.step("Авторизация курьером")
    def auth_courier(self, payload):
            response = requests.post(f"{urls.BASE_URL}/courier/login", json=payload)
            return response

    @allure.step("Получение ID курьера")
    def get_id_from_response(self, response):
            return response.json()["id"]
#
