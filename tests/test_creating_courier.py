import allure 

class TestCourierCreation:

    @allure.title("Проверка создания нового курьера")
    def test_create_courier(self, methods_create_courier):
        payload = methods_create_courier.generate_courier_data()
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"ok": True}
        expected_code = 201
        assert response.status_code == expected_code and response.json() == expected_json

    @allure.title("Проверка кода ответа при создании нового курьера")
    def test_create_courier_check_code(self, methods_create_courier):
        payload = methods_create_courier.generate_courier_data()
        response = methods_create_courier.create_new_courier(payload)

        expected_code = 201
        assert response.status_code == expected_code

    @allure.title("Проверка содержимого ответа при создании нового курьера")
    def test_create_courier_check_json(self, methods_create_courier):
        payload = methods_create_courier.generate_courier_data()
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"ok": True}
        assert response.json() == expected_json    

    @allure.title("Проверка запрета на создания двух курьеров с одинаковыми данными")
    def test_create_duplicate_courier_error(self, methods_create_courier):
        payload_one = methods_create_courier.generate_courier_data()
        first_courier = methods_create_courier.create_new_courier_and_return_data(payload_one)

        payload_two = {"login": first_courier[0], "password": first_courier[1], "firstName": first_courier[2]}
        second_courier = methods_create_courier.create_new_courier(payload_two)

        expected_json = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        expected_code = 409
 
        assert second_courier.status_code == expected_code and second_courier.json() == expected_json

    @allure.title("Проверка запрета на создания двух курьеров с одинаковыми логинами")
    def test_create_duplicate_courier_login_error(self, methods_create_courier):
        payload_one = methods_create_courier.generate_courier_data()
        first_courier = methods_create_courier.create_new_courier_and_return_data(payload_one)

        payload_two = methods_create_courier.generate_courier_data()
        payload_two["login"] = first_courier[0]
        second_courier = methods_create_courier.create_new_courier(payload_two)

        expected_json = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
        expected_code = 409
 
        assert second_courier.status_code == expected_code and second_courier.json() == expected_json

    @allure.title("Проверка запрета на создание курьера без передачи обязательного поля 'login'")
    def test_create_courier_without_login_error(self, methods_create_courier):
        payload = methods_create_courier.generate_courier_data()
        payload["login"] = ""
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
        expected_code = 400

        assert response.status_code == expected_code and response.json() == expected_json

    @allure.title("Проверка запрета на создание курьера без передачи обязательного поля 'password'")
    def test_create_courier_without_password_error(self, methods_create_courier):
        payload = methods_create_courier.generate_courier_data()
        payload["password"] = ""
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
        expected_code = 400

        assert response.status_code == expected_code and response.json() == expected_json    

    @allure.title("Проверка успешного создания курьера без передачи поля 'firstName'")
    def test_create_courier_without_firstname_error(self, methods_create_courier):
        payload = methods_create_courier.generate_courier_data()
        payload["firstName"] = ""
        response = methods_create_courier.create_new_courier(payload)

        expected_json = {"ok": True}
        expected_code = 201

        assert response.status_code == expected_code and response.json() == expected_json        

