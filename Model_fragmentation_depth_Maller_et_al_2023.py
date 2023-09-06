#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 09:58:09 2023

@author: maller
"""


import os
clear = lambda: os.system('clear')
clear()


def Radius(Rp,Fr,uue):  
    
    #impactor radius for a given Fr, relative impact velocity, and target planet radius
    
    return Rp / ((Fr/(2*(uue**2)))-1)


def continuity_parameter(Fr_cut,P,overturns):
    
    #calculates the continuity parameter to link the model on impact
    #and the model of brakup of a turbulent thermal

    a = 0.97
    a2 = a/(1.94**(1/8))
    alpha = 0.07
    
    c1 = 3*alpha/2
    c2 = (P*((P+1)**0.5))/(P+2)
    c3 = Fr_cut**(3/4)
    c4 = (a2*((P+1)**(1/8)))**2

    b = overturns / (c1*c2*c3*c4)   
    
    return b


def f1(fm,rho_m,rho_s):
    
    #sub function of the model
    
    b = (rho_m - rho_s)/(fm*rho_m + (2-fm)*rho_s)
    c = (fm*rho_m + (1 - fm)*rho_s)/rho_s
    
    f = fm * b * (c**(3/4))
    
    return f


def crater_COM(R,RRt,fm,rho_m,rho_s,UUe):
    
    #calculates the center of mass of the crater 
    
    a = (3**(3/4))/4
    b = R*((1 + 1/RRt)**(1/4))
    c = (fm*((rho_m-rho_s)/rho_s) + 1)**(1/4)
    d = (UUe)**(1/2)
    
    COM = a * b * c * d
    
    return COM


def thermal_length(Rc, n, b, fm, rho_m, rho_s, RRt, UUe):
    
    #calculates the length of the transit of the metal core
    #in the magma ocean post-impact before fragmentation 
    
    a = 0.97/(1.94**(1/8))
    alpha = 0.07
    
    c1 = 3/(2**(1/4))
    c2 = f1(fm,rho_m,rho_s)
    c3 = (1 + 1/RRt)**(3/4)
    c4 = (UUe)**(3/2)
    
    tz = Rc*(n - b*(a**2)*alpha*c1*c2*c3*c4)
    
    return tz


def model_equation(Rc, n, b, fm, rho_m, rho_s, RRt, R, UUe):
    
    #first segment of the equation is the crater center of gravity
    a = crater_COM(R,RRt,fm,rho_m,rho_s,UUe)
    
    #second segment of the equation is the transition in the magma ocean
    b1 = thermal_length(Rc, n, b, fm, rho_m, rho_s, RRt, UUe)
    
    z = a + b1
    
    return z,a,b1

      
def one_point(RcR, Fr_cut ,n, fm, rho_m, rho_s, Rplanet, UUe,R):
    
    #density constrast for planets
    P = fm*((rho_m - rho_s)/rho_s)
   
    #continuity parameter
    b = continuity_parameter(Fr_cut,P,n)
    
    #core radius
    Rc = RcR*R
    
    #impactor to target radius ratio
    RRt = R/Rplanet
    
    #getting the depth
    Z,COM,diff = model_equation(Rc, n, b, fm, rho_m, rho_s, RRt, R, UUe)
    
    return Z



def the_model(R,R_planet,UUe):
    #R and R_planet in km
    #UUe is the ratio of impact velociy over escape velocity
    
    #Criterion on frag in the magma ocean
    nt = 7
    n_p = 4

    #Criterion on frag upon impact
    Frt = 40
    Frp = 10

    #physical parameters
    fm = 0.16       #volume fraction of metal
    rho_m = 8000    #density metal
    rho_s = 4000    #density silicates
    RcR = fm**(1/3) #core radius on total radius ratio
    
    #Impact Fr from impact parameters
    Fr = 2*(1 + R_planet/R)*(UUe**2)
    
    #center of mass of the crater
    COM = crater_COM(R,R/R_planet,fm,rho_m,rho_s,UUe)
    
    #We return 
    #   1 - the state of fragmentation upon impact
    #   2 - the depth of total fragmentation in km (0 if on impact)
    #   3 - the depth of partial fragmetation in km (0 if on impact)
    #   4 - the center of mass of the crater
    
    if Fr > 40:
        
        return 'total frag. on impact', 0, 0, COM
    
    elif Fr > 10:
        
        return 'partial frag. on impact', \
            one_point(RcR, Frt ,nt, fm, rho_m, rho_s, R_planet, UUe,R), \
                0, COM
    
    else:
        
        return 'no frag. on impact',\
            one_point(RcR, Frt ,nt, fm, rho_m, rho_s, R_planet, UUe,R),\
                one_point(RcR, Frp ,n_p, fm, rho_m, rho_s, R_planet, UUe,R), COM
                
                
            
    
    


