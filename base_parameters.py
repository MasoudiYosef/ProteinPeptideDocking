import numpy as np
from math import *
def get_parameters():
    f=open('Base.txt','r')
    l=f.readline()
    base=[]
    while len(l)>0:
        l=l.replace('\n','')
        l=l.split(',')
        base.append(l)
        l=f.readline()
    f.close()
    return base

def get_ligand(file):
    f=open(file,'r')
    atom=f.readline()
    atoms=[]
    while len(atom)>0:
        if atom[0:4]=='ATOM':
            serial=atom[6:11].replace(' ','')
            name=atom[11:16].replace(' ','')
            x=atom[31:39].replace(' ','')
            y=atom[39:47].replace(' ','')
            z=atom[47:55].replace(' ','')
            o=atom[55:61].replace(' ','')
            t=atom[61:67].replace(' ','')
            p=atom[67:77].replace(' ','')
            at=atom[77:79].replace(' ','')
            atoms.append([serial,name,float(x),float(y),float(z),o,t,p,at])
        atom=f.readline()
    f.close()
    return atoms

def get_root(file):
    f=open(file,'r')
    atom=f.readline()
    atoms=[]
    while (atom[0:4]!='ROOT')&(len(atom)>0):
        atom=f.readline()
    atom=f.readline()
    while (atom[0:7]!='ENDROOT')&(len(atom)>0):
        if atom[0:4]=='ATOM':
            serial=atom[6:11].replace(' ','')
            name=atom[11:16].replace(' ','')
            x=atom[31:39].replace(' ','')
            y=atom[39:47].replace(' ','')
            z=atom[47:55].replace(' ','')
            o=atom[55:61].replace(' ','')
            t=atom[61:67].replace(' ','')
            p=atom[67:77].replace(' ','')
            at=atom[77:79].replace(' ','')
            atoms.append([serial,name,x,y,z,o,t,p,at])
        atom=f.readline()
    f.close()
    return atoms

def get_branch(file):
    f=open(file,'r')
    line=f.readline()
    branches=[]
    while len(line)>0:
        if (line[0:6]=='BRANCH')&(len(line)>0):
            start=line[6:10].replace(' ','')
            end=line[10:14].replace(' ','')
            branches.append([start,end])
        line=f.readline()
    f.close()
    branch_list=[]
    for i in range(0,len(branches)):
        f=open(file,'r')
        lst=[]
        while 1:
            line=f.readline()
            if line[0:4]=='ATOM':
                start=line[6:11].replace(' ','')
                if (branches[i][0]==start):
                    while 1:
                        if line[0:4]=='ATOM':
                            serial=line[6:11].replace(' ','')
                            lst.append(serial)
                        end=branches[i][1]
                        line=f.readline()
                        if line[0:9]=='ENDBRANCH':
                            s=line[9:13].replace(' ','')
                            e=line[13:17].replace(' ','')
                            if (s==start)&(e==end):
                                break
                    branch_list.append(lst)
                    f.close()
                    break
    return branches,branch_list

def select_atoms(R,L):
    from math import sqrt
    SA=[]
    for i in range(0,len(R)):
        x1=float(R[i][2])
        y1=float(R[i][3])
        z1=float(R[i][4])
        for j in range (0,len(L)):
            x=float(L[j][2])
            y=float(L[j][3])
            z=float(L[j][4])
            dis=sqrt(pow(x-x1,2)+pow(y-y1,2)+pow(z-z1,2))
            if dis<4.72:
                SA.append(R[i])
                break
    return SA

def select_closet(L,P):
    from math import sqrt
    l=len(L)
    x=float(P[0])
    y=float(P[1])
    z=float(P[2])
    a=float(L[0][2])
    b=float(L[0][3])
    c=float(L[0][4])
    dis=sqrt(pow(x-a,2)+pow(y-b,2)+pow(z-c,2))
    j=0
    for i in range(1,len(L)):
        a=float(L[i][2])
        b=float(L[i][3])
        c=float(L[i][4])
        d=sqrt(pow(x-a,2)+pow(y-b,2)+pow(z-c,2))
        if d<dis:
            dis=d
            j=i
    return j

def set_ligand(L):
    x=np.random.rand()
    y=np.random.rand()
    z=np.random.rand()
    for i in range(0,len(L)):
        L[i][2]=L[i][2]+x
        L[i][3]=L[i][3]+y
        L[i][4]=L[i][4]+z
    return L

def RMSD(Ligand,L):
    r=0
    for i in range(0,len(Ligand)):
        x=pow(L[i][2]-Ligand[i][2],2)
        y=pow(L[i][3]-Ligand[i][3],2)
        z=pow(L[i][4]-Ligand[i][4],2)
        r=x+y+z
    r=r/len(L)
    return sqrt(r)
