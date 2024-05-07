import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, ValidationError
from utils.HTTPMethod import Http_methods
from utils.write_to_exel import ExcelWriter

base_url = 'https://krasnoyarsk.220-volt.ru/tracker_advcake/'

class Product(BaseModel):
    id: str
    name: str

class Get_220:
    def __init__(self):
        self.http = Http_methods()
        self.excel = ExcelWriter(filename='products.xlsx', save_path='C:\\Users\\TurboPushka\\Desktop\\Work\\Python\\SiteParsing\\Tests\\Exel_files')

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
            try:
                product = Product(**product_data)
                name = product.name.replace('Прожектор JAZZWAY', '', 1).replace('Прожектор светодиодный JAZZWAY', '', 1)
                print(f"Item {idx}: ID: {product.id}, Model: {name}")
                product.name = name
                validated.append(product)
            except ValidationError as e:
                print(f"Ошибка валидации товара {idx}: {e}")
        print("Валидация данных прошла успешно")

        assert len(validated) > 0, "Ответ не содержит продуктов"
        assert response.status_code == 200, f"Статус ответа не равен 200, он равен {response.status_code}"

        self.excel.write_products_to_excel(validated)
        self.excel.save_excel()
        print("Данные записаны в файл Exel")

        # Найдем цену товара для каждого элемента в validated
        for product in validated:
            # Формируем URL для каждого товара
            url = f'https://krasnoyarsk.220-volt.ru/catalog/prozhektory/jazzway/{product.id}/'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Найдем элемент с классом, содержащим информацию о цене
            price_element = soup.find(class_='price')

            # Извлечем текст с ценой
            price = price_element.text.strip()

            print(f"Цена товара с ID {product.id}: {price}")

        return response

test = Get_220()
test.get_220_info()
