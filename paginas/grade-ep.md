---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: Engenharia de Produção (EP)
permalink: /grade-ep/
---

## Disciplinas obrigatórias
{: .alert .alert-dark}

{% assign disciplinas = site.data.EP | where: 'tipo', 'Obrigatórias' %}

{% for n in (1..10) %}

### {{n}}º semestre
{: .alert .alert-secondary}

{%assign ns = n | downcase %}

{% assign sem = disciplinas | where: 'semestre', ns %}

{% for disc in sem %}
- {% include disciplina-modal.html disciplina=disc curso='EP' %}
{%- endfor -%}

{% endfor %}

## Disciplinas eletivas
{: .alert .alert-dark}

{% assign disciplinas = site.data.EP | where: 'tipo', 'Optativas' %}

{% for n in (1..10) %}

{% assign sem = disciplinas | where: 'semestre', n %}

{% if sem.size > 0 %}

### {{ n }}º semestre
{: .alert .alert-secondary}

{% for disc in sem %}

- {% include disciplina-modal.html disciplina=disc curso='EP' %}

{%- endfor -%}

{% endif %}

{% endfor %}