import xlrd

wb = xlrd.open_workbook('names.xlsx')
sheet = wb.sheet_by_index(0)

# goes through rows in excel and print it out
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))