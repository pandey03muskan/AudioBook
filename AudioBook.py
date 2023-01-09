import PyPDF2
import pyttsx3
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

bg='#3CB371'
white='#ffffff'

root=Tk()
root.geometry("400x500")
root.minsize(500,400)
root.maxsize(700,600)
root.title("AudioBook")
root.configure(bg=bg)

#FUNCTION OF CLICK[to open the pdf]
path=None
def click():
    global path 
    path=filedialog.askopenfilename()
    print(path)
    
#FUNCTION OF READ
def Read():
    page_number=page_box.get()
    if path and page_number:
        #initalization of pyttsx3 module
        speaker=pyttsx3.init()
        #open the pdf
        book=open(path,'rb')
        #read the pdf
        reader=PyPDF2.PdfFileReader(book)
        #choosing the that we want to read
        pages=reader.getPage(int(page_number))
        #extract the text from pdf
        YourBook=pages.extractText()
        #print the text from the page
        print(YourBook)
        speaker.say(YourBook)
        speaker.runAndWait()
    
#FOR LOGO
image=Image.open('book1.png')
imageResizer=image.resize((90,90),Image.LANCZOS)
image1=ImageTk.PhotoImage(imageResizer)
logo=Label(root,image=image1,bg=bg)
logo.pack()

#TITLE OF LOGO
title=Label(root,text="listen your book Now!",bg=bg,font="comicsansms 25 bold",fg=white)
title.pack()

#TAKING INPUT PAGE NUMBER

# 01 text for taking input
pageNumber=Label(root,text="Which page number you want to read",bg=bg,fg=white,font="none 12 bold")
pageNumber.pack(pady=(50,0))

# 02 box of input
page_box=Entry(root,bg=bg,width=40)
page_box.pack(pady=(20,0))

#to open the PDF
openPDF=Button(root,text='open',width=35,command=click)
openPDF.pack(pady=(30,0))

#PDF IS GOING TO SAY SOMETHING
speak_pdf=Button(root,text='Read',width=35,command=Read)
speak_pdf.pack(pady=(20,0))



root.mainloop()





