#!/usr/bin/bash

# Raspar os cursos da EEL

#Obs.: é necessário ter conexão com a internet

# - rodar `python3 raspa_eel.py` para gerar os arquivos json (um por curso)
# - rodar `python3 consolidate-disciplinas-database.py` para gerar os arquivos `disciplinas.json`, `disciplinas.yml` e `cursos.yml`

echo '#' `date`


cd /home/eleno/Dropbox/Lorena/Website/pyjupiter/_python

python3 raspa_eel.py
python3 consolidate-disciplinas-database.py

cp *.yml ../_data

echo

# Geração dos arquivos docx, pdf e xlsx

# Obs.: os arquivos aparecerão em `../assets/disciplinas/`

# - rodar `python3 gera-doc-pdf-unificado.py`
# - rodar `python3 gera-xlsx-unificado.py`

python3 gera-doc-pdf-unificado.py
# python3 gera-xlsx-unificado.py

echo

# Gerar lista de docentes responsáveis

# - rodar `python3 gera_docente_responsavel.py`
 
python3 gera_docente_responsavel.py

echo

# atualiza o site

cd ..

rake build
rake commit

echo
