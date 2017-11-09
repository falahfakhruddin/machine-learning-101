# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Persamaan Garis
Y=mx+c
"""

#Importing Librariees
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing Dataset
dataset= pd.read_csv('data3.txt')
X= dataset.iloc[:, -2].values
Y= dataset.iloc[:, 1].values

#SIgma X dan Y
sig_X =0
sig_Y =0
sig_XX =0
sig_YY =0
sig_XY =0

for i in range (0, len(X)):
    sig_X += X[i]
    sig_Y += Y[i]
    sig_XX += X[i]*X[i]
    sig_YY += Y[i]*Y[i]
    sig_XY += X[i]*Y[i]

#menghituing gradien m dan konstanta c
sxy=sig_XY-(sig_X*sig_Y/len(X))
sxx=sig_XX-(sig_X*sig_X/len(X))
m=sxy/sxx 
    
y_mean=sig_Y/len(Y)
x_mean=sig_X/len(X)
c=y_mean-(m*x_mean)

print (m)
print (c)
