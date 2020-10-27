import requests
import re
from bs4 import BeautifulSoup
import raspa_disciplina as rd


def scrape_curso(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html5lib')

    baseurl = 'https://uspdigital.usp.br/jupiterweb/'
    curso = {}
    semestre = ''
    tipo = ''

    for tr in soup('tr'):

        try:  # testando para semestre
            if tr['bgcolor'] == '#CCCCCC':
                semestre = tr('span')[0].string.split()[0][:-1]
                print('\nsemestre:', semestre)
        except:
            pass

        try:  # testando para tipo (obrigatória/optativa)
            if tr['bgcolor'] == '#658CCF':
                tipo = tr('b')[0].string.split()[1]
                print('\ntipo:', tipo)
        except:
            pass

        try:  # testando para disciplina
            if tr['class'][0] == 'txt_verdana_8pt_gray':
                disciplina = tr('a')[0]
                link = baseurl + disciplina.get('href')
                sigla = disciplina.string.split()[0]
                nome = tr('td')[1].string
                print(sigla, nome)

                curso[sigla] = {}
                curso[sigla]['sigla'] = sigla
                curso[sigla]['nome'] = nome
                curso[sigla]['link'] = link
                curso[sigla]['requisitos'] = {}
                curso[sigla]['tipo'] = tipo
                curso[sigla]['semestre'] = semestre

                # lendo dados da scrape_disciplina
                dados = rd.scrape_disciplina(link)
                curso[sigla] = {**curso[sigla], **dados}
        except:
            pass

        try:  # testando para requisitos
            req = tr('span')[0]
            if req['class'][0] == 'txt_arial_8pt_red':
                requisito = req.string.split('-')
                reqsigla = requisito[0].split()[0]
                reqnome = requisito[1]
                print('\t', reqsigla, reqnome)

                curso[sigla]['requisitos'][reqsigla] = {}
                curso[sigla]['requisitos'][reqsigla]['sigla'] = reqsigla
                curso[sigla]['requisitos'][reqsigla]['nome'] = reqnome
        except:
            pass
            
        try:  # testando para tipo de requisito
            req = tr('td')[1]
            if req['class'][0] == 'txt_verdana_8pt_red':
                reqtipo = req('div')[0].string.strip()
                reqtipo = re.sub(r"\s+", ' ', reqtipo)
                curso[sigla]['requisitos'][reqsigla]['tipo'] = reqtipo
                print('\t', reqtipo)
        except:
            pass

    return curso


def recursive_print_dict(dictio, of, indent=0, start='- '):
    for k, v in dictio.items():
        if isinstance(v, dict):
            of.write('  ' * indent + f'{start}{k}:\n')
            if k == 'requisitos':
                recursive_print_dict(v, of, indent+1)
            else:
                recursive_print_dict(v, of, indent+1, start='')
        else:
            val = f'{v}'.replace('"', '')
            if 'docente' in k:
                of.write('  ' * indent + f'{start}{k}: {val}\n')
            else:
                of.write('  ' * indent + f'{start}{k}: "{val}"\n')
