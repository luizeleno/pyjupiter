---
layout: page
title: Engenharia Física (EF)
permalink: /grade-ef/
---

{% assign lista = '' | split: '' %}
{% for curso in site.data.cursos.EF %}
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

{% assign sem = disciplinas | where: 'semestre.EF', ns %}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EF' %}
{%- endfor -%}

{% endfor %}

## Disciplinas eletivas
{: .alert .alert-dark}

{% assign disciplinas = lista | where: 'tipo', 'Optativas' %}

{% for n in (1..10) %}

{% assign sem = disciplinas | where: 'semestre.EF', n %}

{% if sem.size > 0 %}

### {{ n }}º semestre
{: .alert .alert-secondary}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EF' %}
{%- endfor -%}

{% endif %}

{% endfor %}
