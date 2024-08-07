import json
import os
import xlsxwriter
import row_counter as rc
# from googletrans import Translator
# translator = Translator()


def write(df, field):
    return f'{df[field]}'


def traduzir(texto):
    # try:
    # result = translator.translate(texto)
    # trans = result.text
    # except:
    # print('##Aviso: não foi possível traduzir. Deixando em branco')
    # transl = ''
    return ''  # transl


with open(f'disciplinas.json') as f:
    data = json.load(f)

# print(df.columns.values)

for index, discpln in data.items():

    row = rc.rows()

    print(f'{discpln["sigla"]} - {discpln["nome"]}')

    try:
        os.mkdir(f'../assets/disciplinas/')
    except FileExistsError:
        pass
    docname = f'../assets/disciplinas/{discpln["sigla"]}.xlsx'

    workbook = xlsxwriter.Workbook(docname)
    worksheet = workbook.add_worksheet(f'{discpln["sigla"]}')

    bold = workbook.add_format({'bold': True})
    bold.set_align('top')
    text_wrap = workbook.add_format({'text_wrap': True})
    text_wrap.set_align('top')
    red = workbook.add_format({'text_wrap': True, 'font_color': 'red'})
    red.set_align('top')

    worksheet.set_column('A:B', 30, bold)
    worksheet.set_column('B:B', 60, text_wrap)
    worksheet.set_column('C:C', 60, red)

    r = next(row)
    worksheet.write(r, 1, 'Ementa atual:', bold)
    worksheet.write(
        r, 2, 'Ementa modificada (dados modificados em vermelho):', bold)

    r = next(row)
    worksheet.write(r, 1, write(discpln, 'sigla'))
    worksheet.write(r, 2, write(discpln, 'sigla'))

    r = next(row)
    worksheet.write(r, 0, 'Nome:')
    worksheet.write(r, 1, write(discpln, 'nome'))
    worksheet.write(r, 2, write(discpln, 'nome'))

    r = next(row)
    # worksheet.write(r, 0, 'Name:')
    # worksheet.write(r, 1, write(discpln, 'nome_en'))
    # worksheet.write(r, 2, write(discpln, 'nome_en'))

    if discpln['nome_en']:
        worksheet.write(r, 0, 'Name:')
        worksheet.write(r, 1, write(discpln, 'nome_en'))
        worksheet.write(r, 2, write(discpln, 'nome_en'))
    else:
        text = traduzir(discpln['nome'])
        # worksheet.write(r, 0, 'Name (Google Translator):')
        worksheet.write(r, 0, 'Name:')
        worksheet.write(r, 1, text)
        worksheet.write(r, 2, text)

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
    cs = ''
    for curso, semestre in discpln["semestre"].items():
        cs += f'{curso}-{semestre},'
    worksheet.write(r, 1, cs[:-1])
    worksheet.write(r, 2, cs[:-1])

    r = next(row)
    worksheet.set_row(r, 60)
    worksheet.write(r, 0, 'Objetivos:')
    worksheet.write(r, 1, write(discpln, 'objetivos'))
    worksheet.write(r, 2, write(discpln, 'objetivos'))

    r = next(row)
    worksheet.set_row(r, 60)
    # worksheet.write(r, 0, 'Objectives:')
    # worksheet.write(r, 1, write(discpln, 'objectives'))

    if discpln['objectives']:
        worksheet.write(r, 0, 'Objectives:')
        worksheet.write(r, 1, write(discpln, 'objectives'))
        worksheet.write(r, 2, write(discpln, 'objectives'))
    else:
        text = traduzir(discpln['objetivos'])
        # worksheet.write(r, 0, 'Objectives (Google Translator):')
        worksheet.write(r, 0, 'Objectives:')
        worksheet.write(r, 1, text)
        worksheet.write(r, 2, text)

    ndoc = discpln['ndoc']
    if ndoc:
        r = next(row)
        worksheet.write(r, 0, 'Docentes responsáveis:')
        for doc in discpln["docentes"]:
            r = next(row)
            worksheet.write(r, 1, doc)
            worksheet.write(r, 2, doc)

    r = next(row)
    worksheet.set_row(r, 60)
    worksheet.write(r, 0, 'Programa resumido:')
    worksheet.write(r, 1, write(discpln, 'resumo'))
    worksheet.write(r, 2, write(discpln, 'resumo'))

    r = next(row)
    worksheet.set_row(r, 60)
    # worksheet.write(r, 0, 'Short syllabus:')
    # worksheet.write(r, 1, write(discpln, 'abstract'))
    # worksheet.write(r, 2, write(discpln, 'abstract'))

    if discpln['abstract']:
        worksheet.write(r, 0, 'Short syllabus:')
        worksheet.write(r, 1, write(discpln, 'abstract'))
        worksheet.write(r, 2, write(discpln, 'abstract'))
    else:
        text = traduzir(discpln['resumo'])
        # worksheet.write(r, 0, 'Short syllabus (Google Translator):')
        worksheet.write(r, 0, 'Short syllabus:')
        worksheet.write(r, 1, text)
        worksheet.write(r, 2, text)

    r = next(row)
    worksheet.set_row(r, 120)
    worksheet.write(r, 0, 'Programa:')
    worksheet.write(r, 1, write(discpln, 'programa'))
    worksheet.write(r, 2, write(discpln, 'programa'))

    r = next(row)
    worksheet.set_row(r, 120)
    # worksheet.write(r, 0, 'Syllabus:')
    # worksheet.write(r, 1, write(discpln, 'program'))
    # worksheet.write(r, 2, write(discpln, 'program'))

    if discpln['program']:
        worksheet.write(r, 0, 'Syllabus:')
        worksheet.write(r, 1, write(discpln, 'program'))
        worksheet.write(r, 2, write(discpln, 'program'))
    else:
        text = traduzir(discpln['program'])
        # worksheet.write(r, 0, 'Syllabus (Google Translator):')
        worksheet.write(r, 0, 'Syllabus:')
        worksheet.write(r, 1, text)
        worksheet.write(r, 2, text)

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
            worksheet.write(
                r, 1, f"{req['sigla']} - {req['nome']} ({req['tipo']})\n")
            worksheet.write(
                r, 2, f"{req['sigla']} - {req['nome']} ({req['tipo']})\n")

    workbook.close()
