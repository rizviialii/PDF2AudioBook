import PyPDF2
import pyttsx3
import pdfplumber

file = "sample.pdf"
#file name and "read binary"
pdfFileObject = open(file, 'rb')

#reader
pdfReader = PyPDF2.PdFileReader(pdfFileObject)

pages = pdfReader.numPages

with pdfplumber.open(file) as pdf:
    for i in range(pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()