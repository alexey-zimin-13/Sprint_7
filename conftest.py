import pytest
from methods.methods_creating_courier import MethodsCreatingCourier
from methods.methods_login_courier import MethodsLoginCourier
from methods.methods_create_orders import MethodsCreatingOrder
from methods.methods_get_list_of_orders import MethodsGetList

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
