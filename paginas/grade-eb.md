---
layout: page
title: Engenharia Bioquímica (EB)
permalink: /grade-eb/
---

{% assign lista = '' | split: '' %}
{% for curso in site.data.cursos.EB %}
    {% assign disc = site.data.disciplinas | where: 'sigla', curso %}
    {% assign lista = lista | concat: disc %}
{% endfor %}


## Disciplinas obrigatórias
{: .alert .alert-dark}

{% assign disciplinas = lista | where: 'tipo', 'Obrigatórias' %}

{% for n in (1..10) %}

### {{n}}º semestre
{: .alert .alert-secondary}

{%assign ns = n | downcase %}

{% assign sem = disciplinas | where: 'semestre.EB', ns %}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EB' %}
{%- endfor -%}

{% endfor %}

## Disciplinas eletivas
{: .alert .alert-dark}

{% assign disciplinas = lista | where: 'tipo', 'Optativas' %}

{% for n in (1..10) %}

{% assign sem = disciplinas | where: 'semestre.EB', n %}

{% if sem.size > 0 %}

### {{ n }}º semestre
{: .alert .alert-secondary}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EB' %}
{%- endfor -%}

{% endif %}

{% endfor %}
