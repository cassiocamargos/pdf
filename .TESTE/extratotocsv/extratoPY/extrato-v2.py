from pathlib import Path
import pdftotext
import re
import csv

dir = sorted(Path('/mnt/c/Users/AiO-04/documents/Cassio/Conversor/pdf/TESTE/extratotocsv/testePDF').glob('*.pdf'))

for file in dir:    
  print('\n\n')
  
  namepdf = file.name
  print(namepdf)

  namecsv = file.name
  namecsv = namecsv[:-4] + '.csv'
  print(namecsv)

  with open(namecsv, "w", encoding = 'utf-8') as c:
    writer= csv.writer(
        c,
        delimiter = ';',
        lineterminator = '\n'
    )

    with file.open('rb') as f:    
      pdf = pdftotext.PDF(f)

    table = []

    for page in pdf:
      #print(page)
      lines = page.split('\n')

      for line in lines:
        #print(line)
        date = re.findall(r'([\d]{1,2}/[\d]{1,2}/[\d]{4})',line)
        lanc = re.findall(r'[\d]{1,2}/[\d]{1,2}/[\d]{4}\s+(.+)(?=\s+[\d]{6})',line, flags=re.I)
        dcto = re.findall(r'\b[\d]{6}\b',line)
        valores = re.findall(r'[\S]{0,10}[\.]{0,1}[\d]{0,3},[\d]{0,2}',line)
        valor = valores[0:1]

        date = date[0] if date else 0
        lanc = lanc[0] if lanc else 0
        dcto = dcto[0] if dcto else 0
        valor = valor[0] if valor else 0

        lanc = lanc.strip() if lanc!=0 else 0
        
        row = [date, lanc, dcto, valor]
        #print(row)

        if date == 0:
          del row
        elif dcto == 0:
          del row
        else:
          print(row)
          table.append(row)
          
    writer.writerows(table)