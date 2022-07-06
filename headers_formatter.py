# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:55:40 2022

@author: cnco
"""

with open('C:\\Users\\cnco\\Downloads\\headers.txt','r') as f:
    txt=f.readlines()

newtxt=[]
for i in range(len(txt)):
    print(i)
    line=txt[i]
    splitline=line.split(': ')
    if len(splitline)==2:
        splitline[0]="'"+splitline[0]+"'"
        splitline[1]="'"+splitline[1].replace("\n","'\n")
        if i==len(txt)-1:
            splitline[1]+="'"
        newline=splitline[0]+": "+splitline[1]
    else:
        import sys
        print('Error : two : were detected')
        sys.exit()
    newtxt.append(newline)

f.close()


with open('C:\\Users\\cnco\\Downloads\\headersformat.txt','w') as f:
    for line in newtxt:
        f.write(line)
    
f.close()