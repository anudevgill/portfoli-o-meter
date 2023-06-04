import tkinter as tk
import pdfplumber

x=tk.Tk()
x.title("File Uploader")


def btn():
    with pdfplumber.open("Resume.pdf") as pdf:
        resume = pdf.pages[0]
        print(resume.extract_text())

button = tk.Button(x,text="Upload File",command=btn)
button.pack()
x.mainloop()