import json
import raspa_curso as rc

EA = 'EA', '251', '0'
EB = 'EB', '152', '0'
EF = 'EF', '301', '0'
EM = 'EM', '202', '0'
EP = 'EP', '351', '4'
EQD = 'EQD', '052', '1'
EQN = 'EQN', '052', '4'

for curso, codigo, hab in [EF, EM, EA, EB, EP, EQD, EQN]:
    URL = f'https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=88&codcur=88{codigo}&codhab={hab}&tipo=N'
    print(URL)

    dados = rc.scrape_curso(URL)
    with open(f'../_data/{curso}.yml', 'w') as f:
        rc.recursive_print_dict(dados, f)

    with open(f'{curso}.json', 'w') as f:
        json.dump(dados, f)
