import requests
import random
import string
import urls
import allure

class MethodsCreatingCourier:

    @allure.step("Сгенерировать данные курьера")
    def generate_courier_data(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        login = generate_random_string(10)
        password = generate_random_string(10)
        firstName = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }

        return payload
    
    @allure.step("Создать нового курьера")
    def create_new_courier(self, payload):
       
        try:
            response = requests.post(f"{urls.BASE_URL}/courier", json=payload)
            return response
        except requests.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            return []

    @allure.step("Создать нового курьера и вернуть его данные")
    def create_new_courier_and_return_data(self, payload):
        
        login_pass = []

        try:
            response = requests.post(f"{urls.BASE_URL}/courier", json=payload)
        except requests.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            return []

        if response.status_code == 201:
            login_pass.append(payload["login"])
            login_pass.append(payload["password"])
            login_pass.append(payload["firstName"])
    
        return login_pass
    


