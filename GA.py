from first_CS import first_CS
from base_parameters import RMSD
from score import score_population
from score import change_Ligand
from Trader import select_bests
import numpy as np
import copy
    
    
def crossover(CS):
    for i in range(0,round(len(CS)/3)):
        f1=np.random.randint(len(CS))
        f2=np.random.randint(len(CS))
        k1=np.random.randint(len(CS[0]))
        k2=np.random.randint(len(CS[0]))
        if k1>k2:
            k1,k2=k2,k1
        CS[f1][k1:k2],CS[f2][k1:k2]=CS[f2][k1:k2],CS[f1][k1:k2]
        


def mutation(CS):
    for i in range(0,round(len(CS)/3)):
        k=np.random.randint(len(CS))
        for j in range(0,k):
            r=np.random.randint(len(CS[0]))
            m=np.random.randint(2)
            f=-1
            if m==1:
                f=1
            if r<3:
                l=-5
                h=5
                CS[k][r]=CS[k][r]+f*np.random.uniform(low=l, high=h, size=(1,))[0]
            else:
                h=20
                CS[k][r]=CS[k][r]+f*np.random.randint(round(h))
        


def selection(CS,nob,bests):
    C=copy.deepcopy(CS)
    for i in range(0,len(bests)):
        d=round(bests[i][0])
        CS[i]=C[d]



def GA(L,R,B,BRA,BRAI,Lname):
    f=open('poses/'+Lname+'.txt','a')
    f.write('DE algorithm was performed\n\n\n')
    f.write('The native pose of atoms\n')
    for i in range(0,len(L)):
        for j in range(0,5):
            f.write(str(L[i][j])+'\t')
        f.write('\n')
    for it in range(1,2):
        nop=50
        nob=round(nop/3)
        noi=3
        ls=[]
        CS=first_CS(nop,len(BRA))
        OF=score_population(L,R,B,CS,BRA,BRAI)
        rm=[]
        rm.append('GA')
        rm.append(Lname)
        rm.append(str(it))
        for i in range(0,noi):
            crossover(CS)
            mutation(CS)
            OF=score_population(L,R,B,CS,BRA,BRAI)
            bests=select_bests(OF,nob)
            selection(CS,nob,bests)
            CS[nob:nop]=first_CS(nop-nob,len(BRA))
            ls.append(OF[round(bests[0][0])])
            s=round(bests[0][0])
            Lig=change_Ligand(CS[s],copy.deepcopy(L),BRA,BRAI)
            rmsd=RMSD(L,Lig)
            rm.append(str(rmsd))
            for j in range(0,4):
                for i in range(0,len(ls)):
                    rm.append(ls[i][j])
            print('ELC, vdW, SLV, and HB energies in the '+str(i+1)+'th step are:\n',OF[round(bests[0][0])])
            Lig=change_Ligand(CS[s],copy.deepcopy(L),BRA,BRAI)
            f.write('\n\n\nThe predicted pose of the atoms in the '+str(i+1)+'th step \n')
            for i in range(0,len(Lig)):
                for j in range(0,5):
                    f.write(str(Lig[i][j])+'\t')
                f.write('\n')
