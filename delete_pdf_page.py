# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:37:54 2020

@author: punchy[Natnaree S. L.]
"""

from PyPDF2 import PdfFileWriter,PdfFileReader
import os

pdf_path = r'PATH_TO_PDF' #path to your pdf folder 

extn = '.pdf'
for filename in os.listdir(pdf_path):
    if extn in filename:
        filepath = os.path.join(pdf_path,filename)
        print(filename)
        input_pdf = PdfFileReader(filepath,strict=False)#Get every page_NUM in the folder
        page_NUM = input_pdf.getPage(NUMBER_OF_PAGE_YOU_WANT_TO_GET) #ex. 1 
        
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(page_NUM)


        newfilename = filename + '.pdf'
        newfilepath = os.path.join(pdf_path,newfilename)
        os.rename(filepath,newfilepath)
        with open(newfilepath,"wb") as output:
            pdf_writer.write(output)
                 
            