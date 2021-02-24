---
layout: page
title: Engenharia de Produção (EP)
permalink: /grade-ep/
---

{% assign lista = '' | split: '' %}
{% for curso in site.data.cursos.EP %}
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

{% assign sem = disciplinas | where: 'semestre.EP', ns %}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EP' %}
{%- endfor -%}

{% endfor %}

## Disciplinas eletivas
{: .alert .alert-dark}

{% assign disciplinas = lista | where: 'tipo', 'Optativas' %}

{% for n in (1..10) %}

{% assign sem = disciplinas | where: 'semestre.EP', n %}

{% if sem.size > 0 %}

### {{ n }}º semestre
{: .alert .alert-secondary}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EP' %}
{%- endfor -%}

{% endif %}

{% endfor %}
