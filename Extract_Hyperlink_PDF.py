# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:21:23 2022

@author: cnco
"""

# Import necessary packages
import PyPDF2
import pandas as pd

# Open The File in the Command
file = open("C:\\Users\\cnco\\Perso\\Immo\\Guide-achat-immobilier-2022.pdf", 'rb')
PDF = PyPDF2.PdfFileReader(file)
mylist = []
page_numbers = []
key = '/Annots'
uri = '/URI'
ank = '/A'

for page in range(PDF.numPages-1):
    print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            try:
                u = a.getObject()
                if uri in u[ank].keys():
                        url=u[ank][uri]
                        url=url.split('#')[0]
                        if 'http' in url and url!='https://www.immobilier-danger.com/':
                            page_numbers.append(page)
                            mylist.append(url)
                            print(url)
            except KeyError:
                pass
            
df = pd.DataFrame(data={'Page Number':page_numbers,'URL':mylist}).drop_duplicates()
df.to_csv('fileoutput.csv',sep=';',decimal=',')