import pandas
import os
import xlsxwriter
import row_counter as rc

cursos = ['EA', 'EB', 'EF', 'EM', 'EP', 'EQD', 'EQN']

for curso in cursos:

    print(f' {curso} '.center(60, '#'))
    
    df = pandas.read_json(f'{curso}.json', orient='index')
    
    try:
        os.mkdir(f'../assets/cursos/{curso}')
    except FileExistsError:
        pass
    docname = f'../assets/cursos/{curso}/docentes-{curso}.xlsx'
    
    workbook = xlsxwriter.Workbook(docname)
    worksheet = workbook.add_worksheet(f'{curso}')
    
    bold = workbook.add_format({'bold': True})
    rule = workbook.add_format({'top': 1})
    
    worksheet.set_column('A:A', 12)
    worksheet.set_column('B:B', 48)
    worksheet.set_column('C:C', 12)
    worksheet.set_column('D:D', 48)
    
    row = rc.rows()

    r = next(row)
    worksheet.write(r, 0, f'{curso}', bold)

    r = next(row)
    worksheet.write(r, 0, 'Sigla', bold)
    worksheet.write(r, 1, 'Nome', bold)
    worksheet.write(r, 2, 'NUSP', bold)
    worksheet.write(r, 3, 'Docente', bold)
    
    for index, discpln in sorted(df.iterrows()):
        
        print(f'{discpln["sigla"]} - {discpln["nome"]}')
        
        r = next(row)
        worksheet.write(r, 0, discpln['sigla'], rule)
        worksheet.write(r, 1, discpln['nome'], rule)
        
        ndoc = discpln['ndoc']
        if ndoc:
            for i in range(ndoc):
                dados_doc = (discpln['docentes'][i]).split(' - ')
                if i == 0:
                    worksheet.write(r, 2, dados_doc[0], rule)
                    worksheet.write(r, 3, dados_doc[1], rule)
                else:
                    worksheet.write(r, 2, dados_doc[0])
                    worksheet.write(r, 3, dados_doc[1])
                if i < ndoc-1:
                    r = next(row)

    workbook.close()
