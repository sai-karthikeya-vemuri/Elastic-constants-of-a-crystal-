import numpy as np
import matplotlib.pyplot as plt 
def Elastic_Modulus(C,direction):
    """
    This function calculates the Elastic modulus of a crystal in any arbitrary crystallographic direction

    Input -- 
    C - an array of Elastic constants of single crystal in the order of C11,C22,C44
    direction- an array of size 3 which specifies the direction along which we want the Elastic Modulus
    Output --
    Elastic modulus in the given direction in GPa
    """
    s11=(C[0]+C[1])/((C[0]-C[1])*(C[0]+2*C[1]))
    s12=(C[1])/((C[0]-C[1])*(C[0]+2*C[1]))
    s44=1/C[2]
    direction=direction/np.linalg.norm(direction)
    alpha =np.dot(direction,[1,0,0])
    beta =np.dot(direction,[0,1,0])
    gamma =np.dot(direction,[0,0,1])
    val = s11 - (2*(s11-s12)-s44)*((alpha*beta)**2+(alpha*gamma)**2+(beta*gamma)**2)
    E=1/val
    return E
c11=165.6
c12=63.9
c44=79.5
C=np.array([c11,c12,c44])
unit=[]
n=3
for i in range(0, n):
    print("Enter vector component", i, ":")
    item = int(input())
    unit.append(item)

print("The elastic modulus(GPa) in the given direction is:",Elastic_Modulus(C,unit))
