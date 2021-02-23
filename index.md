---
layout: page
title: Projeto PyJupiter
---

**PyJupiter:** simplificando o Júpiter da USP usando raspagem de páginas (_webscraping_) 
{: .lead}

<div class="text-center">
<div class="col-md-2 float-md-right mx-2 my-2">
<a id="no-ext-link" href='https://github.com/luizeleno/pyjupiter' target='_blank'>
<img class='figure-img img-fluid rounded w-100 mx-auto' src='{{site.baseurl}}/assets/images/logos/github.png'>
Código no Github
</a>
</div>
</div>

Há muito tempo o [Sistema Júpiter](https://uspdigital.usp.br/jupiterweb/){: target='_blank'} da [Universidade de São Paulo](https://www5.usp.br/){: target='_blank'} (USP) merece melhorias; no entanto, não as recebe, e não sabemos bem o porquê. A atualização do antigo sistema `uspdigital` para o novo [Portal de Serviços](https://portalservicos.usp.br/){: target='_blank'} foi um banho de água fria para aqueles com alguma esperança de mudanças reais, pois recebemos apenas uma nova [carenagem](https://pt.wikipedia.org/wiki/Carenagem){: target='_blank'} num carro cujo motor ainda é o da internet 1.0.

O projeto [PyJupiter](https://github.com/luizeleno/pyjupiter){: target='_blank'} surgiu para tentar contornar a situação. Aproveitando a eficiência, motivação e proatividade do alunos do curso de [Engenharia Física](http://www.demar.eel.usp.br/grad/){: target='_blank'} do [Departamento de Engenharia de Materiais](http://www.demar.eel.usp.br/){: target='_blank'} da [Escola de Engenharia de Lorena](https://site.eel.usp.br/){: target='_blank'} da [Universidade de São Paulo](https://www5.usp.br/){: target='_blank'} (EEL-USP), usamos **modernas técnicas de _webscraping_ em python** para extrair os dados do Sistema Júpiter.

<div class='alert alert-success' markdown='1'>
## :blue_book: **Como usar:** acesse os cursos da EEL usando o menu no topo da página

- Acesse as disciplinas de cada curso no menu _**Cursos**_
  - Escolha a disciplina. Uma janela se abrirá com o conteúdo encontrado no Júpiter
  - Ao final da página algumas opções estão disponíveis:
    - Acessar a a página da disciplina no Júpiter
    - Salvar como `pdf`
    - Salvar como `docx`
    - Salvar um arquivo `xlsx` (planilha eletrônica).
- Use o campo de busca para pesquisar por disciplinas específicas, independentemente do curso. *Obs.:* o mecanismo de busca diferencia entre caracteres com e sem acentos!
  
:bulb: O arquivo `xlsx` é especial: ele foi criado pensando na reformulação de ementas. O arquivo tem basicamente duas colunas. Na primeira estão os dados atuais. Na segunda, os dados estão repetidos em vermelho. Os dados desta coluna podem ser editados para reformular a ementa e então enviados ao coordenador do curso.
</div>

Por enquanto, extraímos apenas dados das disciplinas da EEL, ainda sem informações de turmas, horários, número de vagas e professores ministrantes. Mas já conseguimos gerar as ementas de todas as nossas disciplinas em arquivos `pdf`, `docx` e `xlsx`, o que pode auxiliar também na reformulação dessas ementas visando as novas DCNs.

Para o futuro, o plano é estender a raspagem para mais detalhes dos cursos e disciplinas, além de, ainda mais adiante, montar uma plataforma para a criação de grades horárias pela Comissão de Graduação da EEL. É um plano de longo prazo, com trabalho "da meia-noite às seis" a ser feito pela [equipe]({{site.baseurl}}/equipe/) de voluntários e alunos de conclusão de curso que se interessarem pelo projeto.

