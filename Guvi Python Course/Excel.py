import xlrd

loc = ("C:\\Users\\hp\Desktop\\Country-Code.xlsx")

wbs = xlrd.open_workbook(loc)

sheet = wbs.sheet_by_index(0)
print(sheet.cell_value(0.0))