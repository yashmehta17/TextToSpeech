import PyPDF2
import pyttsx3 as ts
book = open('C:/Users/GAGAN CHORDIA/Desktop/JavaDA.pdf','rb')#between the first quotes add the location of the pdf file
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
for num in range(0,pages):
    page = reader.getPage(num)
    text = page.extractText()
    x=ts.init()
    x.say(text)
    x.runAndWait()
