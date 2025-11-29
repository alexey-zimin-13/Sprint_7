import allure
import data
import random

class TestOrdersListFields:

    @allure.title("Проверка наличия ожидаемых полей в случайном заказе")
    def test_field_in_order(self, methods_get_orders):
        expected_fields = data.expected_fields

        response = methods_get_orders.get_orders_list()
        status_code = response.status_code
        data_json = response.json()
        number = random.randint(0, len(data_json["orders"]))
        one_order = data_json["orders"][number]

        assert status_code == 200 and set(one_order.keys()) == expected_fields