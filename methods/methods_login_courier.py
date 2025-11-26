import requests
import urls
import allure

class MethodsLoginCourier:

    @allure.step("Авторизация курьером")
    def auth_courier(self, payload):
        
        try:
            response = requests.post(f"{urls.BASE_URL}/courier/login", json=payload)
            return response
        except requests.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            return []
    

    @allure.step("Получение ID курьера")
    def get_id_from_response(self, response):
  
        if response.status_code == 201 and "id" in response.json():
            return response.json()["id"]
        return ('ID не получен!')
