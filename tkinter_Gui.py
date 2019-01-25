# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from selenium import webdriver
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

def InstalledCheck():
        bat_file = "ps1run.bat"
        os.system(bat_file)
        txt = open('Updatelist.txt','r',encoding="UTF-16LE")
        Alist = []
        data = 0

        for line in txt:
                
                if data == 0 and 'インストール済みの更新' not in line:
                        pass
                elif 'インストール済みの更新' in line:
                        data = 1
                        pass          
                elif 'インストール済み更新表示終了' in line:
                        break
                                 
                else:
                        Alist.append(line)

                        


                       
                
        
                
                    
        listbox.insert(0,*Alist)








def Messageboxinfo():
    messagebox.showinfo("情報","しばし待たれーい")  # 情報ダイアログ表示


def Multithread1(self):
        if __name__ == "__main__":
                m = threading.Thread(target = Messageboxinfo)
                u = threading.Thread(target = Updatelistimport)
   
   
                m.start()
                u.start()

def Multithread2(self):
        if __name__ == "__main__":
                m = threading.Thread(target = Messageboxinfo)
                i = threading.Thread(target = InstalledCheck)
   
   
                m.start()
                i.start()

#UpdateCheck_ボタン 
ucButton=tk.Button(text=u'UpdateCheck',width=12)  
ucButton.place(x=12, y=20)
ucButton.bind("<Button-1>",Multithread1)



    

        

#UpdateDownload_ボタン
upButton = tk.Button(text=u'InstalledCheck',width=12)
upButton.place(x=12, y=60)
upButton.bind("<Button-1>",Multithread2)


        
        


#Windows update list text のインポート、又text内のupdatelist判別





        
                

        



























root.mainloop()