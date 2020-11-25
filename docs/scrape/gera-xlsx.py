import pandas
import os
import xlsxwriter


def rows():
    n = 0
    while True:
        yield n
        n += 1

def write(df, field):
    return f'{df[field]}'


cursos = ['EA', 'EB', 'EF', 'EM', 'EP', 'EQD', 'EQN']

for curso in cursos:

    print(f' {curso} '.center(60, '#'))

    df = pandas.read_json(f'{curso}.json', orient='index')

    # print(df.columns.values)

    for index, discpln in df.iterrows():

        row = rows()

        print(f'{discpln["sigla"]} - {discpln["nome"]}')

        try:
            os.mkdir(f'../{curso}')
        except FileExistsError:
            pass
        docname = f'../{curso}/{discpln["sigla"]}.xlsx'

        workbook = xlsxwriter.Workbook(docname)
        worksheet = workbook.add_worksheet(f'{discpln["sigla"]}')
        
        bold = workbook.add_format({'bold': True})
        bold.set_align('top')
        text_wrap = workbook.add_format({'text_wrap': True})
        text_wrap.set_align('top')
        red = workbook.add_format({'text_wrap': True, 'font_color':'red'})
        red.set_align('top')
        
        worksheet.set_column('A:B', 30, bold)
        worksheet.set_column('B:B', 60, text_wrap)
        worksheet.set_column('C:C', 60, red)
        
        r = next(row)
        worksheet.write(r, 1, 'Ementa atual:', bold)
        worksheet.write(r, 2, 'Ementa modificada (dados modificados em vermelho):', bold)
        
        r = next(row)
        worksheet.write(r, 1, write(discpln, 'sigla'))
        worksheet.write(r, 2, write(discpln, 'sigla'))

        r = next(row)
        worksheet.write(r, 0, 'Nome:')
        worksheet.write(r, 1, write(discpln, 'nome'))
        worksheet.write(r, 2, write(discpln, 'nome'))

        r = next(row)
        worksheet.write(r, 0, 'Name:')
        worksheet.write(r, 1, write(discpln, 'nome_en'))
        worksheet.write(r, 2, write(discpln, 'nome_en'))

        r = next(row)
        worksheet.write(r, 0, 'Créditos-aula:')
        worksheet.write(r, 1, write(discpln, 'CA'))
        worksheet.write(r, 2, write(discpln, 'CA'))

        r = next(row)
        worksheet.write(r, 0, 'Créditos-trabalho')
        worksheet.write(r, 1, write(discpln, 'CT'))
        worksheet.write(r, 2, write(discpln, 'CT'))

        r = next(row)
        worksheet.write(r, 0, 'Carga horária:')
        worksheet.write(r, 1, write(discpln, 'CH'))
        worksheet.write(r, 2, write(discpln, 'CH'))

        r = next(row)
        worksheet.write(r, 0, 'Ativação:')
        worksheet.write(r, 1, write(discpln, 'ativacao'))
        worksheet.write(r, 2, write(discpln, 'ativacao'))

        r = next(row)
        worksheet.write(r, 0, 'Semestre ideal:')
        worksheet.write(r, 1, write(discpln, 'semestre'))
        worksheet.write(r, 2, write(discpln, 'semestre'))

        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Objetivos:')
        worksheet.write(r, 1, write(discpln, 'objetivos'))
        worksheet.write(r, 2, write(discpln, 'objetivos'))

        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Objectives:')
        worksheet.write(r, 1, write(discpln, 'objectives'))
        worksheet.write(r, 2, write(discpln, 'objectives'))

        ndoc = discpln['ndoc']
        if ndoc:
            r = next(row)
            worksheet.write(r, 0, 'Docentes responsáveis:')
            for i in range(ndoc):
                r = next(row)
                worksheet.write(r, 1, f'{discpln["docentes"][i]}')
                worksheet.write(r, 2, f'{discpln["docentes"][i]}')

        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Programa resumido:')
        worksheet.write(r, 1, write(discpln, 'resumo'))
        worksheet.write(r, 2, write(discpln, 'resumo'))

        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Short syllabus:')
        worksheet.write(r, 1, write(discpln, 'abstract'))
        worksheet.write(r, 2, write(discpln, 'abstract'))

        r = next(row)
        worksheet.set_row(r, 120)
        worksheet.write(r, 0, 'Programa:')
        worksheet.write(r, 1, write(discpln, 'programa'))
        worksheet.write(r, 2, write(discpln, 'programa'))

        r = next(row)
        worksheet.set_row(r, 120)
        worksheet.write(r, 0, 'Syllabus:')
        worksheet.write(r, 1, write(discpln, 'program'))
        worksheet.write(r, 2, write(discpln, 'program'))

        r = next(row)
        worksheet.write(r, 0, 'Avaliação:')
        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Método:')
        worksheet.write(r, 1, write(discpln, 'metodo'))
        worksheet.write(r, 2, write(discpln, 'metodo'))
        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Critério:')
        worksheet.write(r, 1, write(discpln, 'criterio'))
        worksheet.write(r, 2, write(discpln, 'criterio'))
        r = next(row)
        worksheet.set_row(r, 60)
        worksheet.write(r, 0, 'Norma de recuperação:')
        worksheet.write(r, 1, write(discpln, 'exame'))
        worksheet.write(r, 2, write(discpln, 'exame'))

        r = next(row)
        worksheet.set_row(r, 120)
        worksheet.write(r, 0, 'Bibliografia:')
        worksheet.write(r, 1, write(discpln, 'bibliografia'))
        worksheet.write(r, 2, write(discpln, 'bibliografia'))

        reqs = discpln['requisitos']
        if reqs:
            r = next(row)
            worksheet.write(r, 0, 'Requisitos:')
            for k, req in reqs.items():
                r = next(row)
                worksheet.set_row(r, 30)
                worksheet.write(r, 1, f"{req['sigla']} - {req['nome']} ({req['tipo']})\n")
                worksheet.write(r, 2, f"{req['sigla']} - {req['nome']} ({req['tipo']})\n")

        workbook.close()

        # break

    # break
