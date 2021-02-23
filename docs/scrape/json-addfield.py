import json
import unidecode
import raspa_curso as rc

cursos = ['EF', 'EM', 'EA', 'EB', 'EP', 'EQD', 'EQN']

for curso in cursos:

    with open(f'{curso}.json') as f:
        data = json.load(f)

    for disc in data:
        nome = data[disc]['nome']
        data[disc]['nomeascii'] = unidecode.unidecode(nome)
        with open(f'../_data/curso}.yml', 'w') as f:
            rc.recursive_print_dict(data, f)