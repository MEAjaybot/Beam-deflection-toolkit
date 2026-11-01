
# This file keep the function of five beam 
import numpy as np

def ss_center_point(x, L, P, E, I):
    x = np.asarray(x)
    constant = P / (48 * E * I)

    y = np.where(
        x <= L / 2,
        constant * x * (3 * L**2 - 4 * x**2),
        constant * (L-x) * (3 * L**2 - 4 * (L-x)**2)
    )

    return y



def ss_off_center_point(x,L,a,P,E,I):
    x = np.asarray(x)
    b = L - a
    constant = P/( 6 * E * I * L)

    y = np.where(
        x <= a,
        constant *  b * x * (L**2 - b**2 - x**2),
        constant * a * (L - x) * (2 * L * x - x**2 - a**2)
    )

    return y 
    

def ss_uniform(x,L,w,E,I):
    x = np.asarray(x)
    
    return  w * x * (L**3 - 2 * L * x**2 + x**3)/(24 * E * I)

def cantilever_point(x,L,P,E,I):
    x = np.asarray(x)
    return P * x**2 * (3 * L - x)/(6 * E * I)

def cantilever_uniform(x,L,w,E,I):  
    x = np.asarray(x)
    return w * x**2 * (6 * L**2 - 4 * L * x + x**2)/(24 * E * I)
   
