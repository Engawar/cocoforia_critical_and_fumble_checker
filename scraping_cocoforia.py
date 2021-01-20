# -*- coding: utf-8 -*-
#ココフォリアログの吸い上げ ver.1.0

#ライブラリ
from bs4 import BeautifulSoup
import re

#このプログラムはココフォリア(ccfolia.com)のログに対応しています。
#Ver.1.0では決定的成功と致命的失敗のみを抽出することが可能です。


path = r"任意のココフォリアのmainログ.html"

with open(path,'r') as f:
    file = f.read()

soup = BeautifulSoup(file,'html.parser')


li = []
for i in soup.select("span"):
    li.append(i.getText())

turn = [li[i:i+3] for i in range(0,len(li),3)]

#turnリストの0番目と2番目の整形
for ls in turn:
    ls[0] = ls[0].removeprefix(' ')
    ls[2] = ls[2].replace('\n','')
    ls[2] = ls[2].removeprefix('        ')
    ls[2] = ls[2].removesuffix('      ')
    #ls[2]にクリティカル=決定的成功、ファンブル=致命的失敗があったらcmd,terminal上で表示
    if re.search(r'\s決定的成功',ls[2]) != None:
        print(ls)
    elif re.search(r'\s致命的失敗',ls[2]) != None:
        print(ls)
