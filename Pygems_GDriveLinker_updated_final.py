from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import *
import tkinter as tk
from tkinter.font import Font
import webbrowser
from tkinter import ttk
from tkinter import filedialog,messagebox
import pyperclip
import csv
import os

username = os.getlogin()













window =tk.Tk()
main_menu=tk.Menu(window)

#-----------------main gui title-----------------
window.title("PyGems G-Drive Linker")

wi_gui=720
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

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    listOfFiles = []
    a=txt.get()
    b=a.split('/')
    c=b[5].split('?')
    # print(c[0])
    tttt=c[0]

    # query = f"'1XItNg77h4gW_YJTcjTIfmC4KTEx-RXYR' in parents"

    query = "'{}' in parents".format(tttt)

    page_token = None
    while True:
        response = service.files().list(
            q=query,
            fields="nextPageToken, files(id, name)",
            pageToken=page_token,
            includeItemsFromAllDrives=True, 
            supportsAllDrives=True
        ).execute()

        for file in response.get('files', []):
            listOfFiles.append(file)

        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

       #--------------------------------------------------------
    nam=[]
    main.dlink=[]

	

    for x in listOfFiles:
	    nam.append("https://drive.google.com/"+"uc?id="+x['id']+"&export=download")
	    main.dlink.append([x['name'],"https://drive.google.com/"+"uc?id="+x['id']+"&export=download"])
    

    ml= int(max(len(x[0]) for x in main.dlink))

    # headers = ["Available Direct Download Links From Shared Folder  :" ]
    # row_format ="{:<8}" # left or right align, with an arbitrary '8' column width 

    listbox.insert(0,"File Name :"+"  "*67+"Direct links :")

   
    for items in main.dlink:
    	listbox.insert(END, items[0]+"  "*(ml-len(items[0]))+"   #"+items[1])

    #----------------------------------------------------
  

# ----------- Functions -------------

def pygems():
	messagebox.showerror("Error", "Incorrect Sharable link")

def past():
	try:
		txt.insert(0, pyperclip.paste())
		a=txt.get()
		b=a.split('/')
		if b[3]=="file":
			dlink="https://drive.google.com/"+"uc?id="+b[5]+"&export=download"
			txt2.insert(0,dlink)
		elif b[3]=="drive":
			main()
		else:
			messagebox.showerror("Error", "Invalid Sharable Link")

	except:
		clear()
		pygems()

	
def copy():
	try:
		a=txt2.get()
		pyperclip.copy(a)
		btn_txt.set("Copied")
	except:
		messagebox.showerror("Error", "Have Nothing To Copy")


def scopy():
	try:
		value=listbox.get(listbox.curselection())
		N,L=value.split("#")
		pyperclip.copy(L)
		cccbtn.set("Copied")
		cccbtn.set("Copy")
	except:
		messagebox.showerror("Error", "Select Any Link First")

	


def lcopy():
	try:	
		file = open(f'C:\\Users\\{username}\\Desktop\\PyGems_GDrive_Linker.csv', 'w', newline ='') 
		  
		with file: 
		    # identifying header
		    write = csv.writer(file)   
		    write.writerow(["File Name","Direct Links"]) 
		    # writing data row-wise into the csv file 
		    write.writerows(main.dlink)
		    messagebox.showinfo("PyGems GDrive Linker","Exported To your Desktop")
		path=f'C:\\Users\\{username}\\Desktop\\PyGems_GDrive_Linker.csv'
		os.startfile(path)
	except:
		messagebox.showerror("Error", "Have Nothing to Export")




def clear():
	txt.delete(0, 'end')
	txt2.delete(0, 'end')
	listbox.delete(0, 'end')

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
elbl.pack(side=LEFT,padx=90)
clbtn = Button(cframe, text="Clear Fields", command=clear,width=20,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
clbtn.pack(side=LEFT)

cframe.pack(pady=10)


#-----------boxframe -----------

scrollbar = Scrollbar(boxframe)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(boxframe, yscrollcommand=scrollbar.set,width=150)
# for i in range(40):
#     listbox.insert(END, "Newfile :#   https://drive.google.com/")
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)
boxframe.pack(pady=20,padx=10)


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
cclbtn = Button(ccframe, text="Export List", command=lcopy,textvariable=lcbtn,width=20,relief=RAISED,font=('Times 10 bold'),fg='#fcf9ec',bg='#132238')
lcbtn.set("Export List")
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