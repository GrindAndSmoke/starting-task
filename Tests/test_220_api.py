import allure
import pytest
from utils.api import Get_220
from utils.Checking import Checking


@allure.epic("Тестирование методов для Get_220")
class TestGet220Info:

    @allure.description("Тестирование получения информации о продуктах")
    def test_getting_information(self):
        # Создание экземпляра класса Get_220
        get_220 = Get_220()
        result_post = get_220.get_220_info()  # Вызов метода через экземпляр класса
        Checking.check_status_code(result_post, 200)
        print("Тест успешно выполнен")