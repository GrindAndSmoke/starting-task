import openpyxl

class ExcelWriter:
    def __init__(self, filename, save_path):
        self.filename = filename
        self.save_path = save_path

    def write_products_to_excel(self, products):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet['A1'] = 'ID'
        sheet['B1'] = 'Name'

        for idx, product in enumerate(products, start=2):
            sheet[f'A{idx}'] = product.id
            sheet[f'B{idx}'] = product.name

        workbook.save(f"{self.save_path}/{self.filename}")

    def save_excel(self):

        pass
