import allure 

class TestCourierLogin:

    @allure.title("Проверка авторизации курьера")
    def test_auth_courier(self, methods_login_courier, create_courier_for_auth):
        
        response = methods_login_courier.auth_courier(create_courier_for_auth)

        expected_code = 200
        json_data = response.json()

        assert response.status_code == expected_code and 'id' in json_data

    @allure.title("Проверка ошибки при авторизации курьера без логина")
    def test_auth_courier_without_login(self, methods_login_courier, create_courier_for_auth):
        
        create_courier_for_auth["login"] = ""
        
        response = methods_login_courier.auth_courier(create_courier_for_auth)

        expected_code = 400
        expected_json = {"code": 400, "message":  "Недостаточно данных для входа"}
    
        assert response.status_code == expected_code and response.json() == expected_json    

    @allure.title("Проверка ошибки при авторизации курьера без пароля")
    def test_auth_courier_without_password(self, methods_login_courier, create_courier_for_auth):
 
        create_courier_for_auth["password"] = ""

        response = methods_login_courier.auth_courier(create_courier_for_auth)

        expected_code = 400
        expected_json = {"code": 400, "message":  "Недостаточно данных для входа"}
        
        assert response.status_code == expected_code and response.json() == expected_json  

    @allure.title("Проверка ошибки при авторизации с неверным логином")
    def test_auth_courier_wrong_login(self, methods_create_courier, methods_login_courier, methods_generation_couriers, create_courier_for_auth):

        create_courier_for_auth["login"] = "test12345"

        response = methods_login_courier.auth_courier(create_courier_for_auth)

        expected_code = 404
        expected_json = {"code": 404, "message": "Учетная запись не найдена"}
        
        assert response.status_code == expected_code and response.json() == expected_json 

    @allure.title("Проверка ошибки при авторизации с неверным паролем")
    def test_auth_courier_wrong_password(self, methods_login_courier, create_courier_for_auth):

        create_courier_for_auth["password"] = "test12345"

        response = methods_login_courier.auth_courier(create_courier_for_auth)

        expected_code = 404
        expected_json = {"code": 404, "message": "Учетная запись не найдена"}
        
        assert response.status_code == expected_code and response.json() == expected_json 

    @allure.title("Проверка получения ID при авторизации курьера")
    def test_auth_courier(self, methods_login_courier, create_courier_for_auth):
 
        response = methods_login_courier.auth_courier(create_courier_for_auth)

        json_data = response.json()

        assert 'id' in json_data
