# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:59:06 2020

@author: Black lotus
"""


def menu1() :
	print('################################################################################')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                  welcome                                     #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('################################################################################')

def menu2() :
	print('################################################################################')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                      1.Gasoline 95 price 29.15Bath                           #')
	print('#                      2.Gasoline 91 price 25.30Bath                           #')
	print('#                      3.Gasohol 91  price 21.68Bath                           #')
	print('#                      4.Gasohol E20 price 20.2Bath                            #')
	print('#                      5.Gasohol 95  price 21.2Bath                            #')
	print('#                      6.Diesel      price 21.1Bath                            #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('################################################################################')

def menu3() :
	print('################################################################################')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                          1.Money in liters                                   #')
	print('#                                                                              #')
	print('#                          2.liters in Money                                   #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('################################################################################')
menu1()
a = input("Continue please Enter")
menu2() 
y = 1
while y==1:  

    t = input("1.Gasoline 95,2.Gasoline 91,3.Gasohol 91,4.Gasohol E20,5.Gasohol 95,6.Diesel :\nต้องการ =")
    
def menu4() :
	print('################################################################################')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                          1.Money in liters                                   #')
	print('#                                                                              #')
	print('#                          2.liters in Money                                   #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('#                                                                              #')
	print('################################################################################')

	p = input("ผู้ใช้งานเลือกว่าจะคำนวณ : เงินเป็นลิตร : ลิตรเป็นเงิน \nเลือก  = ")
if 'เงินเป็นลิตร' in p :
    		g1 = input('กรุณาใส่จำนวนเงินที่ต้องการ:\n จำนวนเงิน = ')
    		m1 = int(g1)
if 'เงินเป็นลิตร'in p :    
    		if 'Gasoline 95' in t :
    		    k = (m1/29.15)
    		    print('จะได้','%.2f' %k,'ลิตร')
    		elif 'Gasoline 91' in t :
    		    k = (m1/25.30)
    		    print('จะได้','%.2f' %k,'ลิตร')
    		elif 'Gasohol 91' in t :
    		    k = (m1/21.68)
    		    print('จะได้','%.2f' %k,'ลิตร')
    		elif 'Gasohol E20' in t :
    		    k = (m1/20.2)
    		    print('จะได้','%.2f' %k,'ลิตร')
    		elif 'Gasohol 95' in t :
    		    k = (m1/21.2)
    		    print('จะได้','%.2f' %k,'ลิตร')
    		elif 'Diesel' in t :
    		    k = (m1/21.1)
    		    print('จะได้','%.2f' %k,'ลิตร')
elif 'ลิตรเป็นเงิน' in p :
    		g2 = input('กรุณาใส่จำนวนลิตรที่ต้องการ:\n จำนวนลิตร = ')
    		m2 = int(g2)
if 'ลิตรเป็นเงิน' in p :
            if 'Gasoline 95' in t :
                k = (m2*29.15)
                print('ราคาน้ำมัน =',k,'บาท')
    
            elif 'Gasoline 91' in t :
                k = (m2*25.30)
                print('ราคาน้ำมัน =',k,'บาท')
elif 'Gasohol 91' in t :
    		    k = (m2*21.68)
    		    print('ราคาน้ำมัน =',k,'บาท')
elif 'Gasohol E20' in t :
    		    k = (m2*20.2)
    		    print('ราคาน้ำมัน =',k,'บาท')
elif 'Gasohol 95' in t :
    		    k = (m2*21.2)
    		    print('ราคาน้ำมัน =',k,'บาท')
elif 'Diesel' in t :
    		    k = (m2*21.1)
    		    print('ราคาน้ำมัน =',k,'บาท')
else :
    		print("ใส่ชนิดใหม่")
x = int(input("ใส่ 1 หรือ 0"))
if x == 1:
    		y = 1
elif x == 0:
    		y=0

