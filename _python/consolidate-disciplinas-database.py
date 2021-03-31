import json
import recursive_print_dict as rpd

curso_yaml = open('cursos.yml', 'w')

cursos = ['EF', 'EM', 'EA', 'EB', 'EP', 'EQD', 'EQN']

disciplinas = {}

for curso in cursos:

    curso_disc = []

    with open(f'{curso}.json') as f:
        data = json.load(f)

    for key in data.keys():
        sem = data[key]['semestre']
        data[key]['semestre'] = {}
        data[key]['semestre'][curso] = sem

        if key in disciplinas:
            ''' disciplina já adicionada, portanto
                data[key]['semestre'] já é dicionário
            '''
            '''
               TO DO: os tipos dos requisitos podem ser diferentes
               em cursos diferentes! Preciso acertar isso
            '''
            disciplinas[key]['semestre'][curso] = sem 
        else:
            disciplinas[key] = data[key]
        
        curso_disc.append(key)

    print(curso, end=': ', file=curso_yaml)
    print(curso_disc, file=curso_yaml)
    
    with open(f'disciplinas.yml', 'w') as f:
        rpd.RecursivePrintDict(disciplinas, f)

curso_yaml.close()

with open('disciplinas.json', 'w') as f:
    json.dump(disciplinas, f)
