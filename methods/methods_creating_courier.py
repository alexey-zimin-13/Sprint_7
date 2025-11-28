import requests
import urls
import allure

class MethodsCreatingCourier:


    
    @allure.step("Создать нового курьера")
    def create_new_courier(self, payload):
            response = requests.post(f"{urls.BASE_URL}/courier", json=payload)
            return response


    @allure.step("Создать нового курьера и вернуть его данные")
    def create_new_courier_and_return_data(self, payload):
        
        login_pass = []

        response = requests.post(f"{urls.BASE_URL}/courier", json=payload)


        if response.status_code == 201:
            login_pass.append(payload["login"])
            login_pass.append(payload["password"])
            login_pass.append(payload["firstName"])
    
        return login_pass
    


