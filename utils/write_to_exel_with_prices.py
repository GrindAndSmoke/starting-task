import openpyxl

class ExcelWriter_w_prices:
    def __init__(self, filename, save_path):
        self.filename = filename
        self.save_path = save_path

    def write_products_to_excel(self, products):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet['A1'] = 'ID'
        sheet['B1'] = 'Name'
        sheet['C1'] = 'Price'  # Добавляем заголовок для цены

        for idx, product in enumerate(products, start=2):
            sheet[f'A{idx}'] = product.id
            sheet[f'B{idx}'] = product.name
            sheet[f'C{idx}'] = product.price  # Записываем цену

        workbook.save(f"{self.save_path}/{self.filename}")

    def save_excel(self):
        pass
