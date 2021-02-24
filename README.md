# pyjupiter

## Raspagem do Jupiter para os cursos do Demar

## Prof. Luiz T. F. Eleno e equipe
### Depto. de Eng. de Materiais (Demar)
### Escola de Engenharia de Lorena (EEL)
### Universidade de São Paulo (USP)

É com grande prazer que anuncio a primeira etapa do projeto **pyjupiter**, uma tentativa de centralização dos dados das disciplinas de todos os cursos da EEL visando a criação de quadros de horários e a distribuição de carga horária pela CG e pelos departamentos de uma maneira mais fácil.

O trabalho veio do TCC de um aluno meu da EF, o Caio Pages, de webscrapping do Sistema Júpiter usando python. Conseguimos, nesta primeira etapa, criar uma espécie de "Mini Jípiter" local. Já conseguimos gerar as ementas de todas as nossas disciplinas em arquivos pdf e docx, o que pode auxiliar também na reformulação dessas ementas visando as novas DCNs.

Para usar o projeto:

https://computeel.org/pyjupiter/

onde estão todas os cursos da EEL/USP, com ementas ementas em pdf, docx ou xlsx.

Saliento que esse trabalho só foi possível graças à dedicação dos nossos alunos. Parabéns a eles!

## Como usar os códigos python

Para usar o projeto, basta acessar o site acima. No entanto, os interessados podem consultar e rodar os códigos python que estão no diretório `_python`.

### Raspar os cursos da EEL

Obs.: é necessário ter conexão com a internet

- rodar `python3 raspa-EEL.py` para gerar os arquivos json (um por curso)
- rodar `python3 consolidate-disciplinas-database.py` para gerar os arquivos `disciplinas.json`, `disciplinas.yml` e `cursos.yml`

### Geração dos arquivos docx, pdf e xlsx

Obs.: os arquivos aparecerão em `../assets/disciplinas/`

- rodar `python3 gera-doc-pdf-unificado.py`
- rodar `python3 gera-xlsx-unificado.py`

### Gerar lista de docentes responsáveis

- rodar `python3 gera_docente_responsavel.py`
