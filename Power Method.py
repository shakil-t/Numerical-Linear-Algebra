# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:49:17 2019

@author: shakil
"""

import math as m
import numpy as np

def calculate_norm(X, norm):
    if(norm==1):
        Σ=0
        for x in X:
            Σ+=x**2
        return m.sqrt(Σ)
    elif(norm==2):
        Σ=0
        for x in X:
            Σ+=abs(x)
        return Σ
    elif(norm==3):
        return max(np.absolute(X))

def power_method(A, u, ε, norm):
    #for returning U later
    U=u
    
    counter=0
    stop=False
    while not stop:
        counter+=1
        μ=calculate_norm(A@u, norm)
        U=(A@u)/μ
        if(calculate_norm(U-u, norm)<=ε):
            stop=True
            return U, counter
        else:
            u=U

print("Welcome :)")
proceed=True
while(proceed):
    print("Note:")
    print("1.A must be a square matrix so entering the number of rows/columns is just enough!")
    print("2.If A is n*n, b will be n*1!")
    
    #number of rows and columns
    n=int(input("Enter the dimensions of matrix A:"))
    
    #getting A
    l1=[]
    print("Matrix A:")
    for i in range(0, n):
        temp1=[]
        for j in range(0, n):
            index_i=str(i+1)
            index_j=str(j+1)
            index=index_i+","+index_j
            print("Item", index)
            temp1.append(float(input()))
        l1.append(temp1)
        
    #using numpy
    A=np.array(l1)
    print(A)
    print()
    
    #getting u0
    l2=[]
    print("Initial Guess:")
    for i in range(0, n):
        temp2=[]
        for j in range(0, 1):
            index_i=str(i+1)
            index_j=str(1)
            index=index_i+","+index_j
            print("Item", index)
            temp2.append(float(input()))
        l2.append(temp2)
        
    #using numpy
    u=np.array(l2)
    print(u)
    print()
    
    ε=float(input("Enter the ε>0:"))
    print()
    print("Choose a norm:")
    print("1.Euclidean norm")
    print("2.Manhattan norm")
    print("3.Infinity norm")
    norm=int(input())
    print()
    
    answer, steps=power_method(A, u, ε, norm)
    print("The final answer is:")
    print(answer)
    print()
    print("Found in ", steps, "steps.")
    print("Try again?[yes|no]")
    what_to_do=input()
    if(what_to_do=="no"):
        proceed=False
    print()
