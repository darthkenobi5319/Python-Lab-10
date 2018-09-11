# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:04:40 2017

@author: ZHENGHAN ZHANG
"""

#Fahrenheit to Celsius
def FtoC(x):
    y = x/1.8 - 32/1.8
    return format(y,'.2f')

#Celsius to Fahrenheit
def CtoF(x):
    y=32+1.8*x
    return format(y,'.2f')

#main program
def main():
    while True:
        print('-------------------------------')
        print('1.Convert Fahrenheit to Celsius')
        print('2.Convert Celsius to Fahrenheit')
        print('0.Quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            x=int(input('Enter the Fahrenheit:'))
            print('Converted to Celsius is:',FtoC(x))
        elif choice == '2':
            x=int(input('Enter the Celcius: '))
            print('Converted to Fahrenheit is:',CtoF(x))
        elif choice =='0':
            break
        else:
            print('invalid input')
    print('l')

#Execute the program
if __name__ == '__main__':
    main()
    