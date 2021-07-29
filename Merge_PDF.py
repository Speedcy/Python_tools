# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:30:22 2021

@author: cypri
"""

import PyPDF2
import os

os.chdir('C:\\Users\\cypri\\Documents\\Documents Cyprien\\Python Tools')

filename1='5.pdf'
filename2='Pro Git - 5.Git distribué.pdf'
outputname=filename2
merge_method='normal' # normal custom
 
# Open the files that have to be merged one by one
pdf1File = open('Input File/'+filename1, 'rb')
pdf2File = open('Input File/'+filename2, 'rb')
 
# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File, strict=False)
 
# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

if merge_method=='normal':
    # Loop through all the pagenumbers for the first document
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
     
    # Loop through all the pagenumbers for the second document
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

elif merge_method=='custom':
    pdfWriter.addPage(pdf1Reader.getPage(0))
    pdfWriter.addPage(pdf1Reader.getPage(1))
    pdfWriter.addPage(pdf1Reader.getPage(2))
    pdfWriter.addPage(pdf1Reader.getPage(3))
    pdfWriter.addPage(pdf2Reader.getPage(0))
    pdfWriter.addPage(pdf1Reader.getPage(5))
    pdfWriter.addPage(pdf1Reader.getPage(6))
 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('Output File/'+outputname, 'wb')
pdfWriter.write(pdfOutputFile)
 
# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()