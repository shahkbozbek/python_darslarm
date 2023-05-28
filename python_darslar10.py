# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni
 #kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan 
 #savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, 
 #ahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
 #chiqaring.

#mahsulotlar = ["olma", "olma", "behi", "sabzi", "gosh", "non", "kartoshka",]

#savat = []
  
#for n in range(5):
#  savat.append(input(f'Savatga {n+1} mahsulotni qo\'shing>'))
  
#for mahsulot in savat:
    #if mahsulot in mahsulotlar:
     #   print(f"Do'konimizda {mahsulot} bor")
    #else:
     #   print(f"Do'konimizda {mahsulot} yo'q")
#user = ['salim','halim','karim','botir']
#login = input("Login tanlang>>>")
#if login in user:
 #    print("Kechirasiz bu login band!")
#else:
   # print(f"Hush kelibsiz  {login.title()} !") son = input("Ikkita soni kiriting>>>")


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")




















