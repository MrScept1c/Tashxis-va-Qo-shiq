# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jWsafATxdHTct66dob9gaRNUKQhnPTPX
"""

def tashxis(belgi):
  if belgi=="bosh og'rig'i":
    return "Bol nol iching"
  elif belgi=="tish og'rig'i":
    return "stomatologga boring"
  elif belgi=="Isitma":
    return "Parasetamol iching"
  elif belgi=="Qandli diabet":
    return "Shirinlik yemang"
  elif belgi=="Ruhiy kasallik":
    return "Psixologga boring"
  elif belgi=="Gepatit":
    return "Parxez qiling"
  elif belgi =="Covid":
    return "Paxlovid iching"
  else:
    return "Shifokorga murajaat qiling"

belgi=input("Kasallik belgisini kiriting ")
natija=tashxis(belgi)
print(natija)

def singer(qoshiq):
  if qoshiq=="Another love":
    return "Tom odell"
  elif qoshiq=="Happier than even":
    return "Billie Eilish"
  elif qoshiq=="Until I found you":
    return "Stephan Sanchez"
  elif qoshiq== "I wanna be yours":
    return "Arctic Monkeys"
  elif qoshiq== "Meni sev":
    return "Sevara Nazarxon"
  elif qoshiq== "We don't talk anymore":
    return "Charlie Puth"
  elif qoshiq== "See you again":
    return "Wiz khalifa"
  elif qoshiq=="Love yourself":
    return "Justin Bieber"
  elif qoshiq =="Riptide":
    return "Vance Joy"
  elif qoshiq=="Blinding Lights":
    return "The weekend"
  else:
    return "Googledan qidir"
qoshiq=input("Qo'shiq nomini kiriting  ")
natija=singer(qoshiq)
print(natija)