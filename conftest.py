import pytest
from methods.methods_creating_courier import MethodsCreatingCourier
from methods.methods_login_courier import MethodsLoginCourier
from methods.methods_create_orders import MethodsCreatingOrder
from methods.methods_get_list_of_orders import MethodsGetList
from methods.methods_generation_orders_data import MethodsGenerationOrderData
from methods.methods_generation_couriers_data import MethodsGenerationCourierData
from methods.methods_delete_courier import MethodsDeleteCourier

@pytest.fixture
def methods_create_courier():
    return MethodsCreatingCourier()

@pytest.fixture
def methods_login_courier():
    return MethodsLoginCourier()

@pytest.fixture
def methods_create_order():
    return MethodsCreatingOrder()

@pytest.fixture
def methods_get_orders():
    return MethodsGetList()

@pytest.fixture
def methods_generation_orders():
    return MethodsGenerationOrderData()

@pytest.fixture
def methods_generation_couriers():
    return MethodsGenerationCourierData()

@pytest.fixture
def methods_delete_couriers():
    return MethodsDeleteCourier()

@pytest.fixture
def create_courier(methods_generation_couriers, methods_create_courier, methods_login_courier, methods_delete_couriers):
        payload = methods_generation_couriers.generate_courier_data()
        response = methods_create_courier.create_new_courier(payload)
        yield response
        del payload["firstName"]
        response_auth = methods_login_courier.auth_courier(payload)
        id = methods_login_courier.get_id_from_response(response_auth)
        methods_delete_couriers.delete_courier(id)

@pytest.fixture
def create_courier_data(methods_generation_couriers, methods_create_courier, methods_login_courier, methods_delete_couriers):
        payload_one = methods_generation_couriers.generate_courier_data()
        first_courier = methods_create_courier.create_new_courier_and_return_data(payload_one)
        yield first_courier
        del payload_one["firstName"]
        response_auth = methods_login_courier.auth_courier(payload_one)
        id = methods_login_courier.get_id_from_response(response_auth)
        methods_delete_couriers.delete_courier(id)

@pytest.fixture
def create_courier_for_auth(methods_generation_couriers, methods_create_courier, methods_login_courier, methods_delete_couriers):
        payload = methods_generation_couriers.generate_courier_data()
        methods_create_courier.create_new_courier(payload)
        del payload["firstName"]
        response_auth = methods_login_courier.auth_courier(payload)
        id = methods_login_courier.get_id_from_response(response_auth)
        
        yield payload
        
        methods_delete_couriers.delete_courier(id)



