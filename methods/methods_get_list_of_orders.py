import requests
import urls
import allure

class MethodsGetList:

    @allure.step("Получение списка заказов")
    def get_orders_list(self):
        
        try:
            response = requests.get(f"{urls.BASE_URL}/orders")
            return response
        except requests.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            return []
    


