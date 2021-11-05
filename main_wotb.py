#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import tkinter  as tk
import sys  
import win32ctypes.core
import os
from tkinter import filedialog
import plyer 
from tkinter import messagebox
 
def fileo():
    current_directory = plyer.filechooser.open_file()
    return current_directory;
s=fileo()
print("start") 
e=str(s[0]).replace(chr(92), "/") 
df = pd.read_csv (e, sep=';')  
pd.set_option("max_rows", None)
rez=pd.DataFrame(df)
df['PAYED_IN_CURR_AMT'].astype('float')
print("") 
filtra=rez[['ACTION_DT','PAYMENT_CURRENCY','PAYED_IN_CURR_AMT','PAY_ORDER_STATUS_CODE','PAY_AGGREGATOR_DESC','PAY_ITEM_TYPE_NAME','AA_PACKAGE_LIST']] 
all_cost=filtra[['PAY_ORDER_STATUS_CODE','PAYED_IN_CURR_AMT','PAY_AGGREGATOR_DESC']]
cop=3;
a=all_cost.groupby('PAY_ORDER_STATUS_CODE')['PAY_AGGREGATOR_DESC'].value_counts()
suma= all_cost.groupby('PAY_ORDER_STATUS_CODE')['PAYED_IN_CURR_AMT'].sum() 
na=list(a['PAID'].index)
naa=list(a['PAID'].values) 
list_of=[];
for i  in range(len(naa)): 
    list_of.append(na[i] + " " +str(naa[i]) );
root = tk.Tk()
root.geometry("390x150")
root.title("how much money did i spend on the tank")
canvas = tk.Canvas(root,bg='grey') 
ints0 = tk.Label(root,text="how much money did i spend on the tank")
ints0.grid(row=1, column=0,columnspan=2)  
ints1 = tk.Label(root,text="all the purchases you made: ",anchor='w',justify="left",padx=0)
ints1.grid(row=2, column=0,sticky = 'w')  
ints = tk.Label(root,text="money: ",anchor='w',padx=0)
ints2 = tk.Label(root,text=filtra['PAY_ORDER_STATUS_CODE'].value_counts()['PAID'])
ints2.grid(row=2, column=1,sticky = 'w')  
ints3 = tk.Label(root,text=round(suma['PAID'],2))
ints3.grid(row=3, column=1,sticky = 'w')  
ints.grid(row=3, column=0,sticky = 'w')   
my = tk.Label(root,text="mainly used for purchasing:",anchor='w',justify="left",padx=0)
my.grid(row=4, column=0,sticky = 'w') 
Lb1 = tk.Listbox(root,selectmode="BROWSE", height=4)
for i in range(len(naa)): 
    Lb1.insert(i,list_of[i]) 
Lb1.grid(row=4, column=1)  
root.mainloop()