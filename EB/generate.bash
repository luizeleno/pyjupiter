#!/usr/bin/bash

for x in `ls ../docs/EB/*.html`
do
  
  y=`basename $x .html`
  
  echo $y
  wkhtmltopdf $x $y.pdf
  
  abiword --to=docx $y.pdf
done
