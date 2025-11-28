import allure
import pytest


class TestOrderCreation:

    @allure.title("Проверка создания заказа с различным цветом")
    @pytest.mark.parametrize(
        "color",
        [
            (["BLACK"]),
            (["GREY"]),
            (["BLACK", "GREY"]),
            ([])
        ]
    )
    def test_http_status_for_color_options(self, methods_create_order, methods_generation_orders, color):
        payload = methods_generation_orders.generate_order_data(color=color)
        response = methods_create_order.create_order(payload)
        json_data = response.json()

        assert response.status_code == 201 and 'track' in json_data


