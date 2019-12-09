import openpyxl

wb = openpyxl.load_workbook("common.xlsx")
sh = wb["register"]
rows = sh.rows
title = list(map(lambda x: x.value, next(rows)))
print(title)
#### 放大师傅
"""
"""