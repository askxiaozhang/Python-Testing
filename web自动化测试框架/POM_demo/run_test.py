import os
import pytest
from time import sleep

if __name__ == '__main__':
    pytest.main()
    sleep(2)
    os.system('allure generate ./temp -o ./reports --clean')
