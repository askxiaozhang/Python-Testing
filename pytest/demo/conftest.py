import pytest

@pytest.fixture(scope='function',params=['irving','james','paul'])
def pz(request): #pz为自定义名
    print('全局前置')
    yield request.param
    print('全局后置')
