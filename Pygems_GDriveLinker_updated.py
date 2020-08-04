from tkinter import *
import tkinter as tk
from tkinter.font import Font
import webbrowser
from tkinter import ttk
from tkinter import filedialog,messagebox
import pyperclip

window =tk.Tk()
main_menu=tk.Menu(window)

#-----------------main gui title-----------------
window.title("PyGems G-Drive Linker")

wi_gui=700
hi_gui=420

wi_scr=window.winfo_screenwidth()
hi_scr=window.winfo_screenheight()

x=(wi_scr/2)-(wi_gui/2)
y=(hi_scr/2)-(hi_gui/2)

window.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))

# window.iconbitmap(r'C:\Users\HujurHacker\Desktop\Final gui\images\xlsx.ico')

##-------------- All Frames ----------------++

sframe=Frame(window)
dframe=Frame(window)
cframe=Frame(window)
boxframe=Frame(window)
fframe=Frame(window)
ccframe=Frame(window)









# ----------- Functions -------------

def pygems():
	messagebox.showerror("Error", "Incorrect Sharable link")

def past():
	try:
		txt.insert(0, pyperclip.paste())
		a=txt.get()
		b=a.split('/')
		dlink="https://drive.google.com/"+"uc?id="+b[5]+"&export=download"
		txt2.insert(0,dlink)
	except:
		clear()
		pygems()

	
def copy():
	a=txt2.get()
	pyperclip.copy(a)
	ccclbtn.set("Copied")

def scopy():
	try:
		value=listbox.get(listbox.curselection())
		pyperclip.copy(value)
		cccbtn.set("Copied")
		cccbtn.set("Copy")
	except:
		messagebox.showerror("Error", "Select Any Link First")

	


def lcopy():
	all_items = listbox.get(0, tk.END)
	print(all_items)
	lcbtn.set("Copied")


def clear():
	txt.delete(0, 'end')
	txt2.delete(0, 'end')

def opnlink(url):
    webbrowser.open_new(url)


####-------------- sframe ------------

lbl = Label(sframe, text="Google Drive Sharable File Link : ",
	bd=0,
	fg='#F4511E',
	font='Times 12',
	width=0,
	height=0)

lbl.pack(side=LEFT,padx=5)
txt = Entry(sframe,width=60)
txt.pack(side=LEFT,padx=5)

pbtn = Button(sframe, text="Past", command=past,width=10,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
pbtn.pack(side=LEFT,padx=5)

sframe.pack(pady=15)

#------------- dframe -------------------------

lbl2 = Label(dframe, text="               Direct Download Link : ",bd=0,
	fg='#F4511E',
	font='Times 12',
	width=0,
	height=0)
lbl2.pack(side=LEFT,padx=5)


txt2 = Entry(dframe,width=60)
txt2.pack(side=LEFT,padx=5)

btn_txt=StringVar()
cbtn = Button(dframe, text="Copy",textvariable=btn_txt,command=copy,width=10,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
btn_txt.set("Copy")
cbtn.pack(side=LEFT,padx=5)

dframe.pack(pady=10)


#--------------cframe ----------------

elbl = Label(cframe, text="              ")
elbl.pack(side=LEFT,padx=150)
clbtn = Button(cframe, text="Clear Fields", command=clear,width=20,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
clbtn.pack(side=LEFT)

cframe.pack(pady=10)


#-----------boxframe -----------

scrollbar = Scrollbar(boxframe)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(boxframe, yscrollcommand=scrollbar.set,width=90)
for i in range(40):
    listbox.insert(END, "https://drive.google.com/file/d/1NpyIFJP__DTdWd7WaIlDfrOVNxIclBu6/view?usp=sharing")
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)
boxframe.pack(pady=20)


#--------------- copy frame -----
cccbtn=StringVar()
ccclbl = Label(ccframe, text="              ")
ccclbl.pack(side=LEFT,padx=50)
ccclbtn = Button(ccframe, text="Copy Selected",textvariable=cccbtn, command=scopy,width=20,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
cccbtn.set("Copy Selected")
ccclbtn.pack(side=LEFT)


lcbtn=StringVar()
cclbl = Label(ccframe, text="              ")
cclbl.pack(side=LEFT,padx=10)
cclbtn = Button(ccframe, text="Copy List", command=lcopy,textvariable=lcbtn,width=20,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
lcbtn.set("Copy List")
cclbtn.pack(side=LEFT)

ccframe.pack(pady=10)



#----------- status frame ---------
statusbar =Label(window, text="Click here to visit : pygems.com ",
 bd=1,
  relief=SUNKEN,
   bg="#37474F",
   fg='#fcf9ec',
   height=1,
   font="Times 13",
   cursor="hand2",
   width=80
   )

statusbar.bind("<Button-1>", lambda e: opnlink("https://pygems.com/"))
statusbar.pack()

fframe.pack()

#-------------- Frames End --------------------


window.mainloop()