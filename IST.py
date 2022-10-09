from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import speedtest

from PIL import Image, ImageTk, ImageSequence
import time





st=speedtest.Speedtest()

root=Tk()




root.title('SPEED TEST')
root.geometry('500x500+400+100')
root.config(background='#B9D7EA')
label=ttk.Label(root,text='SPEED TEST')
label.grid(row=0,column=1,padx=3,pady=5,sticky='snew')
test=ttk.Button(root,text='TEST SPEED')
test.grid(row=1,column=0,columnspan=2,padx=3,pady=3)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)


#main program

def ist():
	servername=[]
	st.get_servers(servername)
	messagebox.showinfo(title="SPEED TEST",message='Download Speed: {} MBPS\nUpload Speed : {} MBPS'.format(round(st.download()/(1024*1024),2),round(st.upload()/(1024*1024),2)))

test.config(command=ist)






#design

style=ttk.Style()
style.theme_use('clam')
style.configure('TLabel',background='#B9D7EA', foreground='#f4f490',font=('Arial',30))
style.configure('TButton',background='#ffc93c',font=('Arial',20))

style.map('TButton',background=[('pressed','#ed8165')])











root.mainloop()
