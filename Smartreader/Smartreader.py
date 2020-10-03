# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:51:01 2020

@author: ankit.anand
"""

import pyttsx3 as ps
import PyPDF2 as pdf
def readfile():
    file_path=input('Enter the path of file: ')
    file_name=input('Enter the pdf file name: ')
    book =open(file_path+'\\'+file_name+'.pdf','rb')
    pdfReader=pdf.PdfFileReader(book)
    speaker=ps.init()
    inputpage=int(input("Enter the page Number : "))
    page=pdfReader.getPage(inputpage-1)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
