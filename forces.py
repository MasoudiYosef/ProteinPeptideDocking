from math import *
from Rotation import get_teta
from base_parameters import select_closet

def slv(L,R,B):
    sl=0
    sikma=3.5
    for i in range(0,len(L)):
        x1=float(L[i][2])
        y1=float(L[i][3])
        z1=float(L[i][4])
        s1,v1,r1,e1,h1=SV(L[i][8],B)
        for j in range(0,len(R)):
            x2=float(R[j][2])
            y2=float(R[j][3])
            z2=float(R[j][4])
            s2,v2,r2,e2,h2=SV(R[j][8],B)
            dis=sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2))
            if dis<r1+r2:
                sl=sl+(s1*v2+s2*v1)*exp(-pow(dis,2)/(2*pow(sikma,2)))
    return sl

def vdw(L,R,BASE):
    vw=0
    for i in range(0,len(L)):
        x1=float(L[i][2])
        y1=float(L[i][3])
        z1=float(L[i][4])
        s1,v1,r1,e1,h1=SV(L[i][8],BASE)
        if int(h1)==0:
            for j in range(0,len(R)):
                x2=float(R[j][2])
                y2=float(R[j][3])
                z2=float(R[j][4])
                s2,v2,r2,e2,h2=SV(R[j][8],BASE)
                if int(h2)==0:
                    dis=sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2))
                    if dis<=r1+r2:
                        ep=sqrt(e1*e2)
                        sigma=(r1+r2)/2
                        A=4*ep*pow(sigma,12)
                        B=4*ep*pow(sigma,6)
                        vw=vw+A/pow(dis,12)-B/pow(dis,6)
    return vw

def elc(L,R,BASE):
    elec=0
    for i in range(0,len(L)):
        x1=float(L[i][2])
        y1=float(L[i][3])
        z1=float(L[i][4])
        qi=float(L[i][7])
        s1,v1,r1,e1,h1=SV(L[i][8],BASE)
        for j in range(0,len(R)):
            x2=float(R[j][2])
            y2=float(R[j][3])
            z2=float(R[j][4])
            dis=sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2))
            s2,v2,r2,e2,h2=SV(R[j][8],BASE)
            if dis<=r1+r2:
                A=8.5525
                lam=0.003627
                k=7.7839
                eps=78.4
                B=eps-A
                d=1+k*exp(-lam*B*dis)
                d=A+B/d
                qj=float(R[j][7])
                elec=elec+qi*qj/(dis*d)
    return elec

def h_bond(L,R,BASE):
    hb=0
    chb=0
    for i in range(0,len(L)):
        x1=float(L[i][2])
        y1=float(L[i][3])
        z1=float(L[i][4])
        r1,e1,h1=SVh(L[i][8],BASE)
        for j in range(0,len(R)):
            x2=float(R[j][2])
            y2=float(R[j][3])
            z2=float(R[j][4])
            r2,e2,h2=SVh(R[j][8],BASE)
            if (h1>0)|(h2>0):
                dis=sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2))
                ep=max(e1,e2)
                sigma=(r1+r2+1)/2
                if dis<=r1+r2+1:
                    A=5*ep*pow(sigma,12)
                    B=6*ep*pow(sigma,10)
                    chb=chb-1
                    if h1>0:
                        p=select_closet(L,[x1,y1,z1])
                        p=[float(L[p][2]),float(L[p][3]),float(L[p][4])]
                        teta=get_teta([x1,y1,z1],[x2,y2,z2],p)
                    else:
                        p=select_closet(R,[x2,y2,z2])
                        p=[float(R[p][2]),float(R[p][3]),float(R[p][4])]
                        teta=get_teta([x1,y1,z1],[x2,y2,z2],p)
                    if (L[i][8]=='N')|(L[i][8]=='NA')|(L[i][8]=='NS')|(R[j][8]=='N')|(R[j][8]=='NA')|(R[j][8]=='NS'):
                        teta=pow(cos(teta*3.14/180),2)
                    else:
                        teta=pow(cos(teta*3.14/180),4)
                    if teta>90:
                        chb=chb-1
                        hb=hb+A/pow(dis,12)-B/pow(dis,10)*teta                    
    return chb+hb

def SV(at,B):
    s=0
    v=0
    r=0
    e=0
    h=0
    for i in range(0,len(B)):
        if at==B[i][0]:
            s=float(B[i][3])
            v=float(B[i][4])
            r=float(B[i][1])
            e=float(B[i][2])
            h=float(B[i][7])
            break
    return s,v,r,e,h

def SVh(at,B):
    r=0
    e=0
    h=0
    for i in range(0,len(B)):
        if at==B[i][0]:
            r=float(B[i][5])
            e=float(B[i][6])
            h=float(B[i][7])
            break
    return r,e,h
