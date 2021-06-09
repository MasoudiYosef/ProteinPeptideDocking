from base_parameters import select_atoms
from forces import elc
from forces import vdw
from forces import slv
from forces import h_bond
from Rotation import rotation
from Rotation import Rx
from Rotation import Ry
from Rotation import Rz
import numpy as np
import copy

def score(Ligand,Receptor,base):
    Receptor=select_atoms(Receptor,Ligand)
    el=elc(Ligand,Receptor,base)
    vw=vdw(Ligand,Receptor,base)
    sl=slv(Ligand,Receptor,base)
    hb=h_bond(Ligand,Receptor,base)
    return [el,vw,sl,hb]

def change_Ligand(CS,L,BRA,BRAI):
    for i in range(0,len(L)):
        L[i][2]=L[i][2]+CS[0]
        L[i][3]=L[i][3]+CS[1]
        L[i][4]=L[i][4]+CS[2]
        theta=CS[3]
        o=np.round([L[i][2],L[i][3],L[i][4]]*Rx(theta),decimals=4)[0]
        L[i][2]=o[0]
        L[i][3]=o[1]
        L[i][4]=o[2]
        theta=CS[4]
        o=np.round([L[i][2],L[i][3],L[i][4]]*Ry(theta),decimals=4)[0]
        L[i][2]=o[0]
        L[i][3]=o[1]
        L[i][4]=o[2]
        theta=CS[5]
        o=np.round([L[i][2],L[i][3],L[i][4]]*Rz(theta),decimals=4)[0]
        L[i][2]=o[0]
        L[i][3]=o[1]
        L[i][4]=o[2]
    for i in range(6,len(CS)):
        inx=i-6
        s1=BRA[inx][0]
        s2=BRA[inx][1]
        for j in range(0,len(L)):
            if L[j][0]==s1:
                x1=L[j][2]
                y1=L[j][3]
                z1=L[j][4]
                break
        for j in range(0,len(L)):
            if L[j][0]==s2:
                x2=L[j][2]
                y2=L[j][3]
                z2=L[j][4]
                break
        ATL=BRAI[inx]
        k=0
        while k<len(ATL):
            for j in range(0,len(L)):
                if L[j][0]==ATL[k]:
                    o=rotation([x1,y1,z1,x2,y2,z2],[L[j][2],L[j][3],L[j][4]],CS[i])
                    L[j][2]=o[0]
                    L[j][3]=o[1]
                    L[j][4]=o[2]
                    k=k+1
                    if k>=len(ATL):
                        break
    return L
            

def CheckDirection(Lig,L):
    for i in range(0,len(Lig)):
        if (Lig[i][2]*L[i][2]<0)&(Lig[i][3]*L[i][3]<0):
            Lig[i][2]=-Lig[i][2]
            Lig[i][3]=-Lig[i][3]
        if (Lig[i][2]*L[i][2]<0)&(Lig[i][4]*L[i][4]<0):
            Lig[i][2]=-Lig[i][2]
            Lig[i][4]=-Lig[i][4]
        if (Lig[i][3]*L[i][3]<0)&(Lig[i][4]*L[i][4]<0):
            Lig[i][3]=-Lig[i][3]
            Lig[i][4]=-Lig[i][4]
    return Lig
    
    
def score_population(L,R,B,CS,BRA,BRAI):
    OF=np.zeros([len(CS),4])
    for i in range(0,len(CS)):
        Lig=change_Ligand(CS[i],copy.deepcopy(L),BRA,BRAI)
        OF[i]=score(Lig,R,B)
    return OF
