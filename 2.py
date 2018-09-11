# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:26:48 2017

@author: ZHENGHAN ZHANG
"""
#define the function
def reverseList(x):
    y=[]
    for i in range(len(x)):
        y.append(x[-i-1])
    return y

# the main function
def main():
    x = list(input('Enter a string:'))
    print(reverseList(x))
    print(x)
    return

#execute the program
if __name__ =='__main__':
    main()
    