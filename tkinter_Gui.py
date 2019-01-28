# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from selenium import webdriver
import time
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

listbox = tk.Listbox(root,height=30,width=90,selectmode='extended')
listbox.pack()

Alist = []
Blist = []

#メニューバーのラジオボタンで行う関数
def Listselect():
        size = listbox.size()
        
        listbox.delete(0,size)
        
        
        if var.get() == 0:
            listbox.insert(0,*Blist)

        elif var.get() == 1:
            listbox.insert(0,*Alist)




#メニューバー
var = tk.IntVar()
var.set(0)

men = tk.Menu(root)
root.config(menu=men)
menu_select = tk.Menu(root,tearoff = False)
men.add_cascade(label='[           Listselect            ]',menu=menu_select)
men.add_separator()
radiobutton_1 = menu_select.add_radiobutton(label = "Not Installed", value = 0,variable=var,command=Listselect)
radiobutton_2 = menu_select.add_radiobutton(label = "Installed", value = 1,variable=var,command=Listselect)




#updatecheck及びメッセージボックスの関数(マルチスレッド)
# Listの入力と、未インストールとインストール済みの仕分けもここでやっています。  

                         
def UpdateCheck():
    bat_file = "ps1run.bat"
    os.system(bat_file)
    txt = open('Updatelist.txt','r',encoding="UTF-16LE")
    global Blist
    global Alist
    Blist = []
    Alist = []
    data = 0

    for line in txt:
            if  '未インストールの更新' in line:
                    pass
        
            elif '未インストール更新表示終了' in line:
                    break
                     
        
        
            else:
                    Blist.append(line)
      

    for line2 in txt:

            if data == 0 and 'インストール済みの更新' not in line2:
                    pass
            elif 'インストール済みの更新' in line2:
                    data =1
                    pass          
            elif 'インストール済み更新表示終了' in line2:
                    break
                                 
            else:
                    Alist.append(line2)

    if var.get() == 0:
            listbox.insert(0,*Blist)

    elif var.get() == 1:
            listbox.insert(0,*Alist)

                




def Messageboxinfo():
    messagebox.showinfo("情報","しばし待たれーい")  # 情報ダイアログ表示


def Multithread1(self):
        if __name__ == "__main__":
                m = threading.Thread(target = Messageboxinfo)
                u = threading.Thread(target = UpdateCheck)
   
   
                m.start()
                u.start()



#UpdateCheck_ボタン 
ucButton=tk.Button(text=u'UpdateCheck',width=12)  
ucButton.place(x=12, y=20)
ucButton.bind("<Button-1>",Multithread1)




#ここから入力したリストから、名前を取り出し検索。ダウンロード。
def Installerdownload():
        for updatename in Blist:
                

        driver = webdriver.Chrome()



#UpdateDownload_ボタン
upButton = tk.Button(text=u'InstallerDownload',width=12)
upButton.place(x=12, y=60)



        
        

































root.mainloop()