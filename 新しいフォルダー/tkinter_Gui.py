# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

import sys, codecs
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

Blist = []
#updateのクラス   

def Updatelistimport():
    bat_file = "ps1run.bat"
    os.system(bat_file)
    txt = open('Updatelist.txt','r',encoding="UTF-16LE")
    Blist = []

    for line in txt:
            if  '未インストールの更新' in line:
                    pass
        
            elif '未インストール更新表示終了' in line:
                    break
                     
        
        
            else:
                    Blist.append(line)
                    
                    
                    
    listbox.insert(0,*Blist)

    






    


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