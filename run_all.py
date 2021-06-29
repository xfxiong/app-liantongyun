import os
import pytest

if __name__ == '__main__':
    pytest.main(["-s", "--alluredir=./reports", "--clean-alluredir"])
    os.system("allure generate ./reports -o ./reports/html --clean")
