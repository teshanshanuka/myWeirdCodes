# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:59:51 2017

@author: Teshan Shanuka J
"""

from sympy import symbols, solve, exp
from sympy.core.numbers import Float
import numpy as np

A = 1.129241e-3
B = 2.341077e-4
C = 8.775468e-8

a,b,c,x,t,r = symbols('a,b,c,x,t,r')
eq1 = a+b*x+c*x**3-1/t
        
#import csv
with open('Rchart.csv', 'w') as f:
    
    for T in np.arange(293.0, 317.0, 0.1):
        
        s1 = solve(eq1.subs({a:A,b:B,c:C,t:T}))
        
        for s in s1:
            if type(s) == Float and s>0:
                ans = exp(s).evalf() 
#                print(T, ':', ans)
                f.write(str(T)+','+str(ans)+'\n')