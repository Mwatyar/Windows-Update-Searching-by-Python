# -*- coding: utf8 -*-
import sys, codecs
txt = open('Updatelist.txt','r',encoding="UTF-16LE")
Blist = []

for line in txt:
        if  '未インストールの更新' in line:
                pass
        
        elif '未インストール更新表示終了' in line:
                break
        
        
        else:
                Blist.append(line)

listnumber_str = input()
listnumber = int(listnumber_str)
updatename = Blist[listnumber]
print(updatename)
txt.close()


#テスティングテスト