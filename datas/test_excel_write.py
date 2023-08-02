import openpyxl

workbook = openpyxl.load_workbook(r'/datas/新建 XLSX 工作表.xlsx')
sheet = workbook['Sheet1']
res = sheet.cell(row=1, column=1, value='id')
workbook.save(r'C:\Users\yuemia\PycharmProjects\test_guo\datas\新建 XLSX 工作表.xlsx')
