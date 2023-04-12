import requests
import unicodedata
import re
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
    text = text.replace('<BR>', '\n')

    # Patch: correção específica para LOM3015, na norma de recuperação
    # preciso encontrar maneira de evitar a conjunção <NF< ser interpretada como tag
    text = text.replace('<NF<', '&leq;NF&lt;')

    soup = BeautifulSoup(text, 'html5lib')

    for span_tag in soup('span'):

        try:  # dados da disciplina em portugues
            if span_tag['class'][0] == 'txt_arial_8pt_gray':
                if span_tag('pre'):  # por causa de alguma cagada que fizeram nos Objetivos da disciplina no Jupiter
                    dado = span_tag('pre')[0].string.strip()
                else:
                    dado = span_tag.string.strip()
                if dado is not None:
                    dados_br.append(dado)
                    ndados_br += 1
                    #print(dado)
                    #print('-'*30)
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
                #if dado is not None:
                    #print(dado)
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


def raspa_oferecimento(codigo):

    baseurl = 'https://uspdigital.usp.br/jupiterweb/obterTurma?sgldis='
    URL = baseurl + codigo
    
    page = requests.get(URL)
    text = page.text
    text = remove_control_characters(text)
    text = text.replace('<br>', '\n')
    text = text.replace('<BR>', '\n')
    
    oferecimento = {}
    
    # iniciando raspagem
    soup = BeautifulSoup(text, 'html5lib')
    
    div = soup.find_all('div', attrs={'style':'border: 2px solid #658CCF; padding: 5px; border-radius: 5px;'})
    for d in div:

      turma = {}
      
      table = d.find_all('table')
      
      # Processando a primeira tabela (dados)
      keys = table[0].find_all('span', class_="txt_arial_8pt_black")  # rótulos
      items = table[0].find_all('span', class_="txt_arial_8pt_gray")
      
      for k, i in zip(keys, items):
        k1 = re.sub(r"\s+", ' ', k.string[:-1])
        turma[k1] = i.string.strip()
      
      # Processando a segunda tabela (horários)
      keys = table[1].find_all('span', class_="txt_arial_8pt_black")  # rótulos
      items = table[1].find_all('span', class_="txt_arial_8pt_gray")
      
      turma['aulas'] = {}
      for h in range(len(items)//4):
        horario = f'{items[0+4*h].string} {items[1+4*h].string} {items[2+4*h].string}'
        prof = items[3+4*h].string
        turma['aulas'][f'h{h}'] = {}
        turma['aulas'][f'h{h}']['horario'] = horario
        turma['aulas'][f'h{h}']['prof'] = prof
        
      # Processando a terceira tabela (vagas)
      keys = table[2].find_all('span', class_="txt_verdana_8pt_white")  # rótulos
      items_total = table[2].find_all('span', class_="txt_arial_8pt_black")  # total
      items_curso = table[2].find_all('span', class_="txt_arial_8pt_gray")  # por turma
      
      vagas = {}
      vagas[items_total[0].string] = {}
      for k, t in zip(keys,items_total[1:]):
        vagas[items_total[0].string][k.string] = t.string

      for c in range(len(items_curso)//5):
        curso = items_curso[5*c].string.strip()
        vagas[curso] = {}
        for k, t in zip(keys,items_curso[5*c+1:5*c+6]):
          vagas[curso][k.string] = t.string
      
      turma['vagas'] = vagas
      
      # adicionando turma ao dict oferecimento
      oferecimento[turma['Código da Turma']] = turma

    #print(oferecimento)
    
    return oferecimento

if __name__ == '__main__':
    disciplina = 'https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=LOM3226&codcur=88202&codhab=0'
    #dic = {}
    dic = scrape_disciplina(disciplina)
    #print('#'*30)
    #[ print(f'{k}: {v}\n' + '-' * 30) for k, v in dic.items() ]
    disc = 'LOM3226'
    #of = raspa_oferecimento(disc)
    #print(of)
