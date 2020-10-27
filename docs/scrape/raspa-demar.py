import raspa_curso as rc

EF = rc.scrape_curso('https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=88&codcur=88301&codhab=0&tipo=N')
f = open('jupiter-scrap/_data/EF.yml', 'w')
rc.recursive_print_dict(EF, f)
f.close()

EM = rc.scrape_curso('https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=88&codcur=88202&codhab=0&tipo=N')
f = open('jupiter-scrap/_data/EM.yml', 'w')
rc.recursive_print_dict(EM, f)
f.close()
