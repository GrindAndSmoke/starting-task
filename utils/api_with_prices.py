import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, ValidationError
from utils.HTTPMethod import Http_methods
from utils.write_to_exel_with_prices import ExcelWriter_w_prices

base_url = 'https://krasnoyarsk.220-volt.ru/tracker_advcake/'

class Product(BaseModel):
    id: str
    name: str
    price: str = None  # Добавляем поле для цены, устанавливаем значение по умолчанию как None

class Get_220_w_prices():
    def __init__(self):
        self.http = Http_methods()
        self.excel = ExcelWriter_w_prices(filename='products.xlsx', save_path='C:\\Users\\TurboPushka\\Desktop\\Work\\Python\\SiteParsing\\Tests\\Exel_files')

    def get_product_info(self, product_data):
        try:
            name = product_data['name'].replace('Прожектор JAZZWAY', '', 1).replace('Прожектор светодиодный JAZZWAY',
                                                                                    '', 1)
            print(f"ID: {product_data['id']}, Model: {name}",
                  end=", ")  # Выводим ID и модель товара без перевода строки
            url = f'https://krasnoyarsk.220-volt.ru/catalog-{product_data["id"]}/'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Найдем элемент, содержащий информацию о цене
            price_element = soup.find(attrs={'data-product-price': True})

            # Проверяем, найден ли элемент с ценой
            if price_element is not None:
                # Извлекаем значение цены из атрибута
                price = price_element['data-product-price']
                print(f"Price: {price}руб.")
                product = Product(id=product_data['id'], name=name, price=price)
            else:
                print(f"Price: Не удалось найти информацию о цене для товара с ID {product_data['id']}")
                product = Product(id=product_data['id'], name=name)

            return product
        except ValidationError as e:
            print(f"Ошибка валидации товара: {e}")
            return None

    def get_220_info(self):
        print(base_url)
        response = self.http.post(base_url, body={"pageType": 3})
        print(f"Статус кода: {response.status_code}")

        data = response.json()

        assert 'products' in data, "Ответ не содержит информацию о продуктах"
        products = data['products']
        print("Данные о товарах получены")

        validated = []
        for idx, product_data in enumerate(products, start=1):
            product = self.get_product_info(product_data)
            if product:
                validated.append(product)

        print("Валидация данных прошла успешно")

        if validated:
            # Записываем данные в файл Excel
            self.excel.write_products_to_excel(validated)
            self.excel.save_excel()
            print("Данные записаны в файл Excel")
        else:
            print("Ответ не содержит продуктов")

        return response

test = Get_220_w_prices()
test.get_220_info()
