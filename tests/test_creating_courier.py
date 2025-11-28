import allure 

class TestCourierCreation:

    @allure.title("Проверка создания нового курьера")
    def test_create_courier(self, create_courier):

        expected_json = {"ok": True}
        expected_code = 201
        assert create_courier.status_code == expected_code and create_courier.json() == expected_json

    @allure.title("Проверка запрета на создания двух курьеров с одинаковыми данными")
    def test_create_duplicate_courier_error(self, methods_create_courier, create_courier_data):

        payload_two = {"login": create_courier_data[0], "password": create_courier_data[1], "firstName": create_courier_data[2]}
        second_courier = methods_create_courier.create_new_courier(payload_two)

        expected_json = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        expected_code = 409
 
        assert second_courier.status_code == expected_code and second_courier.json() == expected_json

    @allure.title("Проверка запрета на создания двух курьеров с одинаковыми логинами")
    def test_create_duplicate_courier_login_error(self, create_courier_data, methods_create_courier, methods_generation_couriers):

        payload_two = methods_generation_couriers.generate_courier_data()
        payload_two["login"] = create_courier_data[0]
        second_courier = methods_create_courier.create_new_courier(payload_two)

        expected_json = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        expected_code = 409
 
        assert second_courier.status_code == expected_code and second_courier.json() == expected_json

    @allure.title("Проверка запрета на создание курьера без передачи обязательного поля 'login'")
    def test_create_courier_without_login_error(self, methods_create_courier, methods_generation_couriers):
        payload = methods_generation_couriers.generate_courier_data()
        payload["login"] = ""
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
        expected_code = 400

        assert response.status_code == expected_code and response.json() == expected_json

    @allure.title("Проверка запрета на создание курьера без передачи обязательного поля 'password'")
    def test_create_courier_without_password_error(self, methods_create_courier, methods_generation_couriers):
        payload = methods_generation_couriers.generate_courier_data()
        payload["password"] = ""
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
        expected_code = 400

        assert response.status_code == expected_code and response.json() == expected_json    

    @allure.title("Проверка успешного создания курьера без передачи поля 'firstName'")
    def test_create_courier_without_firstname_error(self, methods_create_courier, methods_generation_couriers):
        payload = methods_generation_couriers.generate_courier_data()
        payload["firstName"] = ""
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"ok": True}
        expected_code = 201

        assert response.status_code == expected_code and response.json() == expected_json        

