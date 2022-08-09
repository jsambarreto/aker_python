import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

filename = askopenfilename()

arq = pd.read_excel(filename)

out = open('out.txt', 'w')
maq = arq.maquina
mac = arq.mac
ip = arq.ip
for i,j,q in zip(maq, mac, ip):
  out.write('host '+ i+' {')
  out.write('\n')
  out.write('     hardware ethernet ' +j+';')
  out.write('\n')
  out.write('     fixed-address '+ q+ ';')
  out.write('\n')
  out.write('}')
  out.write('\n')
out.close()

