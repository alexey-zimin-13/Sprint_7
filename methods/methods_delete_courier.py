import requests
import urls
import allure

class MethodsDeleteCourier:

    @allure.step("Удаляем курьера")
    def delete_courier(self, id):
            payload = {"id": id}
            response = requests.delete(f"{urls.BASE_URL}/courier", json=payload)
            return response