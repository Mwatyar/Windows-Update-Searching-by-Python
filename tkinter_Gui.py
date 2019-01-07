# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import sys
import threading 
import os
import socket
import glob


#ウィンドウの生成
root = tk.Tk()
root.title("WindowsUpdate Autoupdate Service")
root.geometry("800x550")


#ウィンドウ上にlistの作成

listbox = tk.Listbox(root,height=15,width=90)
listbox.pack()


#updateのクラス   

def Updatelistimport():
    bat_file = "ps1run.bat"
    os.system(bat_file)

def Messageboxinfo():
    messagebox.showinfo("情報","しばし待たれーい")  # 情報ダイアログ表示


def Multithread(self):
    if __name__ == "__main__":

        m = threading.Thread(target = Messageboxinfo)
        u = threading.Thread(target = Updatelistimport)
   
   
        m.start()
        u.start()
    
    


#UpdateCheck_ボタン
ucButton = tk.Button(text=u'UpdateCheck',width=12)  
ucButton.place(x=10, y=20)
ucButton.bind("<Button-1>",Multithread)


#Windows update list text のインポート、又text内のupdatelist判別
























root.mainloop()