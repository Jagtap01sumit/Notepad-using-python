import os.path
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def newFile():
    global file
    root.title("Untitled_Notepad")

    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All File","*.*"),("Text documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "-NoptePad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitaled.txt",defaultextension=".txt",filetypes=[("All File","*.*"),("Text documents","*.txt")])
        if file=="":
            file=None
        else:
            #save as new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file +"-Notepad"))
            print("file saved")
    else:
        #save the file
        f.open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by code with sumit")

if __name__ == '__main__':
    #Bacis setup
    root=Tk()
    root.geometry("600x700")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("notepadpng.png")

    #Add text Area
    TextArea= Text(root, font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    #Lets create a menu
    Menubar=Menu(root)
    FileMenu=Menu(Menubar,tearoff=0)

    #To open New File
    FileMenu.add_command(label="New",command=newFile)

    #To open already existing file
    FileMenu.add_command(label="open",command=openFile)

    #To Save current file
    FileMenu.add_command(label="save",command=saveFile)

    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quit)
    Menubar.add_cascade(label="File",menu=FileMenu)

    #File Menu Ends


    #Edit Menu starts
    EditMenu=Menu(Menubar,tearoff=0)

    #To add feature cut copy and paste
    EditMenu.add_command(label="cut",command=cut)
    EditMenu.add_command(label="copy",command=copy)
    EditMenu.add_command(label="paste",command=paste)

    Menubar.add_cascade(label="Edit",menu=EditMenu)
    #Edit menu end

    #Help menu start

    Helpmenu=Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label="about_Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=Helpmenu)
    #Help menu End


    root.config(menu=Menubar)

    #Add scroll bar
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()