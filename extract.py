from tkinter import *
import PyPDF2
from tkinter import filedialog
import pyttsx3

root = Tk()
root.title("PDF to audiobook converter")
root.geometry("600x500")
root.configure(background="#e34f4f")


# Open PDF File
def open_pdf():
    # Grab the filename of the PDF file
    open_file = filedialog.askopenfilename(
        initialdir="../Desktop",
        title="Open PDF File",
        filetypes=[("PDF Files", "*.pdf")])

    # Check to see if there is a file
    if open_file:
        # Open the PDF file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # Set the page to read
        page = pdf_file.getPage(0)
        # Extract the text from the pdf file
        page_content = page.extractText()
        text = Label(text="Currently Reading Your PDF file")
        # Read text aloud
        speak = pyttsx3.init()
        speak.say(page_content)
        speak.runAndWait()


instruction_label = Label(root, text="Click Browse to select a PDF file to convert to an audiobook",
                          font="Ariel", bg="#e8de87")
instruction_label.pack()


# Browse dialog button
browse_btn = Button(root, command=open_pdf, text="Browse", font="Ariel", bg="#84e88e", fg="#fff",
                    height=2, width=15)
browse_btn.pack()

# Cancel Button
cancel_btn = Button(root, text="Quit", command=root.destroy, font="Ariel", bg="#84e88e", fg="#fff",
                    height=2, width=15)
cancel_btn.pack()

root.mainloop()


