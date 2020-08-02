from tkinter import *
import webbrowser
import pyperclip



window = Tk()
window.title("PyGems_GDriveLinker")
window.geometry('600x180')


# ----------- Functions -------------
def past():
	txt.insert(0, pyperclip.paste())
	a="Mamun"
	txt2.insert(0,a)
	
def copy():
	a=txt2.get()
	pyperclip.copy(a)
	btn_txt.set("Copied")

def clear():
	txt.delete(0, 'end')
	txt2.delete(0, 'end')

def opnlink(url):
    webbrowser.open_new(url)




lbl = Label(window, text="Google Drive Share Link : ")
lbl.grid(column=0, row=0,pady=13,padx=3)

txt = Entry(window,width=60)
txt.grid(column=1, row=0,pady=13)

pbtn = Button(window, text="Past", command=past,width=10)
pbtn.grid(column=2, row=0,pady=13,padx=5)

lbl2 = Label(window, text="Direct Download Link : ")
lbl2.grid(column=0, row=1)

txt2 = Entry(window,width=60)
txt2.grid(column=1, row=1)

btn_txt=StringVar()
cbtn = Button(window, text="Copy",textvariable=btn_txt,command=copy,width=10)
btn_txt.set("Copy")
cbtn.grid(column=2, row=1)


clbtn = Button(window, text="Clear", command=clear,width=40)
clbtn.grid(column=1, row=2, pady=7)



statusbar =Label(window, text="Click here to visit : pygems.com ",
 bd=1,
  relief=SUNKEN,
   bg="#37474F",
   fg='#fcf9ec',
   height=1,
   font="Times 13",
   cursor="hand2",
   width=66
   )

statusbar.bind("<Button-1>", lambda e: opnlink("https://pygems.com/"))
statusbar.grid(columnspan=3,column=0, row=3, pady=38)




window.mainloop()