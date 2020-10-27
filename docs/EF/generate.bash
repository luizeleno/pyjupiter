#!/usr/bin/bash

for x in `ls ../_site/EF/*.html`
do
  
  y=`basename $x .html`
  
  echo $y
  # wkhtmltopdf $x $y.pdf
  
  abiword --to=docx $y.pdf
done
