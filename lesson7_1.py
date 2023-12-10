import tkinter as tk
from tkinter import ttk
from tkinter import *

#定義窗體
root = Tk()
root.title("高血壓判斷")
root.geometry("400x300")

#控件_標籤
lb1 = Label(root, text='請輸入收縮壓[mmHg]')
lb1.place(x=10, y=10, anchor=NW)

lb2 = Label(root, text='請輸入舒張壓[mmHg]')
lb2.place(x=10, y=40, anchor=NW)

#控件_輸入文字框 [收縮壓]
#entry_1 = Entry(width=30, font=("Arial", 12, "bold"),  bg="white", fg="black", state=NORMAL)
entry_1 = Entry(width=30, state=NORMAL)
entry_1.insert(END, string="")
entry_1.place(x=150, y=10, anchor=NW)

#控件_輸入文字框 [舒張壓]
#entry_2 = Entry(width=30, font=("Arial", 12, "bold"),  bg="white", fg="black", state=NORMAL)
entry_2 = Entry(width=30, state=NORMAL)
entry_2.insert(END, string="")
entry_2.place(x=150, y=40, anchor=NW)

#按紐 Clicked 事件
def btn_1_clicked():
   nSBP = int (entry_1.get()) #收縮壓
   nDBP = int (entry_2.get()) #舒張壓
   str_1=""
   if ( nSBP< 120) and ( nDBP<80):
     str_1="您的血壓分類:" + "正常"
   elif (nSBP>=120 and nSBP<=129) and (nDBP <80):
     str_1="您的血壓分類:" + "血壓升高"
   elif (nSBP>=130 and nSBP<=139) and (nDBP >= 80 and nDBP <= 89 ):
     str_1="您的血壓分類:" + "血壓第一期"
   elif (nSBP >= 140) or (nDBP >= 90 ):
     str_1="您的血壓分類:" + "血壓第二期"
   elif (nSBP >= 130) or (nDBP < 80 ):
     str_1="您的血壓分類:" + "單純收縮期高壓"  
   else:
     str_1="超出範圍,系統無法判定"
   lb4 = Label(root, text=str_1)
   lb4.place(x=10, y=120, anchor=NW)

#控件_按紐
btn_1 = Button(text=" 高血壓判斷 ",  command=btn_1_clicked)
btn_1.place(x=300, y=160, anchor=NW)

root.mainloop()