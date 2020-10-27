import requests
import unicodedata
from bs4 import BeautifulSoup


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def scrape_disciplina(URL):

    disciplina = {}

    labels = ['unidade', 'departamento', 'nome_en']
    labels_br = ['CA', 'CT', 'CH', 'periodicidade', 'ativacao', 'objetivos',
                 'docentes', 'resumo', 'programa', 'metodo', 'criterio',
                 'exame', 'bibliografia']
    labels_en = ['objectives', 'abstract', 'program']

    ndados, ndados_br, ndados_en = 0, 0, 0

    dados_br = []

    page = requests.get(URL)
    text = page.text
    text = remove_control_characters(text)
    text = text.replace('<br>', '\n')
    soup = BeautifulSoup(text, 'html5lib')

    for span_tag in soup('span'):

        try:  # dados da disciplina em portugues
            if span_tag['class'][0] == 'txt_arial_8pt_gray':
                dado = span_tag.string.strip()
                if dado is not None:
                    dados_br.append(dado)
                    ndados_br += 1
                    # print(dado)
                    # print('-'*30)
        except:
            pass

        try:  # dados da disciplina em inglês
            if span_tag['class'][0] == 'txt_arial_8pt_gray':
                dado = span_tag('i')[0].string.strip()
                if dado is not None:
                    disciplina[labels_en[ndados_en]] = dado
                    ndados_en += 1
                    # print(dado)
                    # print('-'*30)
        except:
            pass

        try:  # nome da disciplina em portugues
            if span_tag['class'][0] == 'txt_arial_10pt_black':
                dado = span_tag('b')[0].string.strip()
                # if dado is not None:
                    # print(dado)
        except:
            pass

        try:  # nome da disciplina em inglês
            if span_tag['class'][0] == 'txt_arial_10pt_black':
                dado = span_tag.string.strip()
                if dado is not None:
                    disciplina[labels[ndados]] = dado
                    ndados += 1
                    # print(dado)
        except:
            pass

    # preenchendo dados_br
    ndoc = len(dados_br) - len(labels_br) + 1  # no. de docentes
    disciplina['ndoc'] = ndoc
    # print(len(dados_br), len(labels_br))
    for i in range(6):
        disciplina[labels_br[i]] = dados_br[i]
    for i in range(6):
        disciplina[labels_br[7+i]] = dados_br[6+i+ndoc]
    # preenchendo docentes
    disciplina[labels_br[6]] = dados_br[6:6+ndoc]

    return disciplina


if __name__ == '__main__':
    disciplina = 'https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=LOB1003&codcur=88301&codhab=0'
    dic = {}
    dic = scrape_disciplina(disciplina)
    # for k, v in dic.items():
        # print(f'{k}: {v}')
        # print('-'*30)
