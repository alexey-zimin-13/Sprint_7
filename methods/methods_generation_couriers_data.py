import allure
from helpers.data_generation import DataGeneration

class MethodsGenerationCourierData:
    @allure.step("Сгенерировать данные курьера")
    def generate_courier_data(self):
        
        generate_string = DataGeneration()

        login = generate_string.generate_random_string(10)
        password = generate_string.generate_random_string(10)
        firstName = generate_string.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }

        return payload