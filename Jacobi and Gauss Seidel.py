# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 16:24:29 2018

@author: shakil
"""

import math as m
import numpy as np

def spectral_radius(A, algorithm):
    #finding the matrix form
    D=np.diag(np.diag(A))
    L=np.tril(A)-D
    U=np.triu(A)-D
    if(algorithm==1):
        M=-np.linalg.inv(D)@(L+U)
        eigen_values=np.linalg.eigvals(M)
        eigen_values=np.absolute(eigen_values)
        return max(eigen_values)
    elif(algorithm==2):
        M=-np.linalg.inv(L+D)@U
        eigen_values=np.linalg.eigvals(M)
        eigen_values=np.absolute(eigen_values)
        return max(eigen_values)

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
    
def Jacobi_method(A, b, X, ε, norm):
    #for returning Y later
    Y=X
    
    #finding the matrix form
    D=np.diag(np.diag(A))
    L=np.tril(A)-D
    U=np.triu(A)-D
    M=-np.linalg.inv(D)@(L+U)
    c=np.linalg.inv(D)@b
    
    counter=0
    stop=False
    while not stop:
        counter+=1
        Y=M@X+c
        if(calculate_norm(Y-X, norm)<=ε):
            stop=True
            return Y, counter
        else:
            X=Y

def Gauss_Seidel_Method(A, b, X, ε, norm):
    #for returning Y later
    Y=X
    
    #finding the matrix form
    D=np.diag(np.diag(A))
    L=np.tril(A)-D
    U=np.triu(A)-D
    M=-np.linalg.inv(L+D)@U
    c=np.linalg.inv(L+D)@b
    
    counter=0
    stop=False
    while not stop:
        counter+=1
        Y=M@X+c
        if(calculate_norm(Y-X, norm)<=ε):
            stop=True
            return Y, counter
        else:
            X=Y

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
    
    #getting b
    l2=[]
    print("vector b:")
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
    b=np.array(l2)
    print(b)
    print()
    
    #which method?
    print("Choose a method from below:")
    print("1.Jacobi Method")
    print("2.Gauss Seidel Method")
    algorithm=int(input())
    
    #convergence or unconvergence?
    ρ=spectral_radius(A, algorithm)
    #print(ρ)
    if(ρ>=1):
        print("Sorry, this method is unconvergence!")
        proceed=False
    else:
        ε=float(input("Enter the ε>0:"))
        print()
        print("Choose a norm:")
        print("1.Euclidean norm")
        print("2.Manhattan norm")
        print("3.Infinity norm")
        norm=int(input())
        print()
        
        #getting X0
        l3=[]
        print("Initial Guess:")
        for i in range(0, n):
            temp3=[]
            for j in range(0, 1):
                index_i=str(i+1)
                index_j=str(1)
                index=index_i+","+index_j
                print("Item", index)
                temp3.append(float(input()))
            l3.append(temp3)
            
        #using numpy
        X=np.array(l3)
        print(X)
        print()
        
        if(algorithm==1):
            answer, steps=Jacobi_method(A, b, X, ε, norm)
            print("The final answer is:")
            print(answer)
            print()
            print("Found in ", steps, "steps.")
            print("Try again?[yes|no]")
            what_to_do=input()
            if(what_to_do=="no"):
                proceed=False
            print()
        else:
            answer, steps=Gauss_Seidel_Method(A, b, X, ε, norm)
            print("The final answer is:")
            print(answer)
            print()
            print("Found in ", steps, "steps.")
            print("Try again?[yes|no]")
            what_to_do=input()
            if(what_to_do=="no"):
                proceed=False
            print()
