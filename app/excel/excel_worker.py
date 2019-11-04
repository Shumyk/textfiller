import xlrd


class ExcelWorker:
    @staticmethod
    def get_excel_content(file_path):
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)
        content = list()
        for i in range(sheet.nrows):
            content.append(sheet.cell_value(i, 0))
        return content
