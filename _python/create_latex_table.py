import json
import xlsxwriter

with open('EF.json', 'r') as f:
    data = json.load(f)

workbook = xlsxwriter.Workbook('EF-table.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'sigla')
worksheet.write(0, 1, 'nome')
worksheet.write(0, 2, 'semestre')
worksheet.write(0, 3, 'CA')
worksheet.write(0, 4, 'CT')
worksheet.write(0, 5, 'CH')
worksheet.write(0, 6, 'tipo')

r = 1
for materia in data:
    worksheet.write(r, 0, data[materia]['sigla'])
    worksheet.write(r, 1, data[materia]['nome'])
    worksheet.write(r, 2, data[materia]['semestre'])
    worksheet.write(r, 3, data[materia]['CA'])
    worksheet.write(r, 4, data[materia]['CT'])
    worksheet.write(r, 5, data[materia]['CH'])
    worksheet.write(r, 6, data[materia]['tipo'])
    r += 1
        
workbook.close()