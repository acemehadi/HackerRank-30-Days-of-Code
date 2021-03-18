import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdf_reader = PyPDF2.PdfFileReader(book)
page_count = pdf_reader.numPages
print(page_count)

freind = pyttsx3.init()
page_read = pdf_reader.getPage(5)
text = page_read.extractText()

freind.say(text)
freind.runAndWait()
