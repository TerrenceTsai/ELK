# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:15:28 2018

@author: Gin Huang
pioneer machinery
NTUST_NETWORK RELIABILITY & SERVICE SCIENCE
"""


import numpy as np
import math as mt
#import matplotlib.pyplot as plt

x=np.random.randint(0,101,(4,100)) #random: uniform distribution(0,100)

#evaluate X-bar control chart
#input matrix,x(1,n) 
def XbarCC(x):
    n=np.size(x)
    c4=(4*(n-1))/(4*n-3)
    S=np.std(x,axis=1)
    A3=3/(c4*mt.sqrt(n))
    CL=np.mean(x)
    UCL=CL+A3*S
    LCL=CL-A3*S
    omega=S/c4
    return CL,UCL,LCL,omega

    
#XbarCC test
#x=np.array([[10,20,30,40,50,60,70,80,90,100]])
#CL,UCL,LCL,omega=XbarCC(x)   
#print(CL,UCL,LCL,omega) #check 


#evaluate Process capability index
#input
#mu:target value, 
#c4:estimate sigma by using S/c4
#logic:0(U&L) 1(U) 2(L)


def PCIndex(mu,CL,omega,USL,LSL,logic):
    T=USL-LSL
    Ca=(np.abs(CL-mu)/T)
    if logic==0:
        Cp=(USL-LSL)/(6*omega)
        Cpk=Cp*(1-Ca)        
    elif logic==1:
        Cp=(USL-CL)/(3*omega)
        Cpk=Cp**2
    elif logic==2:
        Cp=(CL-LSL)/(3*omega)
        Cpk=Cp**2
    return Cp,Ca,Cpk




    