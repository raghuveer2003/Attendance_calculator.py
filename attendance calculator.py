from tkinter import *
import numpy as np
import pandas as pd
import tkinter as t
from tkinter import messagebox
from tkinter import filedialog
tl=Tk()
tl.geometry("1000x1000")
tl.title("ml project")
l1=Label(tl,text="Starting Date(same as the format in file) :",fg="maroon1")
l1.grid(row=4,column=1)
no=StringVar()
ip=Entry(tl,textvariable=no,font="bold")
ip.grid(row=5,column=1)
l1=Label(tl,text="Ending Date(same as the format in file) :",fg="maroon1")
l1.grid(row=6,column=1)
n=StringVar()
ip=Entry(tl,textvariable=n,font="bold")
ip.grid(row=7,column=1)
t1=Text(tl,height=40,width=123,bg="old lace")
t1.grid(row=9,column=1)
l1=Label(tl,text="ATTENDENCE CALCULATOR",font="italic",fg="blue")
l1.grid(row=1,column=1)
b1=Button(tl,text="select csv to calculate",bg="lightblue",command=lambda:uf())
b1.grid(row=8,column=1)
def of():
      z=no.get()
      x=n.get()
      fn= filedialog.askopenfilename(initialdir="/Users/user", title="select a excel file",filetypes=(("csv files",".csv"),("all files",".*")))
      return z,x,fn
def uf():
      kn=of()
      df=pd.read_csv(kn[2])
      nu=list(df.iloc[:,:])
      y=np.array(df.iloc[:,1:])
      nu.pop(0)
      if kn[0] not in nu and kn[1] not in nu:
           messagebox.showinfo("tl","starting date and ending dates are invalid/not in list")
      if kn[0] not in nu and kn[1] in nu:
           messagebox.showinfo("tl","starting date is invalid/not in list")
      if kn[0] in nu and kn[1] in nu:
       p1,p2=str(kn[0]),str(kn[1])
       d1=df.columns.get_loc(p1)
       d2=df.columns.get_loc(p2)
       t1.delete('1.0','end')
       t1.insert('1.0','Rollno'+'\n'+'\n')
       t1.insert('1.20','\t'+'\t'+'present days')
       t1.insert('1.6','\t'+'\t'+'total days')
       t1.insert('1.33','\t'+'\t'+'absent days')
       k=[]
       for j in range(len(y)):
             l=[]
             for i in range(d1,d2+1):
                 l.append(y[j][i-1])
             k.append(l)
       b,c=[],[]
       for i in range(len(k)):
            b.append(k[i].count('p'))
            c.append(k[i].count('a'))
       sa=[]
       q1=df["Roll No"]
       for u in range(len(b)):
             sa.append(b[u]+c[u])
       for k in range(len(b)):
            t1.insert('end',q1[k]+'\t'+'\t'+"   "+str(sa[k])+'\t'+'\t'+"   "+str(b[k])+'\t'+'\t'+"   "+str(c[k])+'\n')
      if kn[1] not in nu and kn[0] in nu:
           messagebox.showinfo("tl","ending date is invalid/not in list")
