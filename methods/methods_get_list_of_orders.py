import requests
import urls
import allure

class MethodsGetList:

    @allure.step("Получение списка заказов")
    def get_orders_list(self):
            response = requests.get(f"{urls.BASE_URL}/orders")
            return response

    


