from first_CS import first_CS
from base_parameters import RMSD
from score import score_population
from score import change_Ligand
from Trader import select_bests
import numpy as np
import copy
      

def move(CS,bests):
    for i in range(0,len(CS)):
        f=np.random.randint(len(bests))
        k=np.random.randint(len(CS[0]))
        if i != round(bests[0][0]):
            for j in range(0,k):
                s=round(bests[0][0])
                r=np.random.randint(len(CS[0]))
                m=np.random.randint(2)
                d=1
                if m==1:
                    d=-1
                if r<3:
                    CS[i][r]=CS[i][r]+CS[s][r]*d*np.random.rand()
                else:
                    CS[i][r]=CS[i][r]+CS[s][r]*d*np.random.randint(20)


def PSO(L,R,B,BRA,BRAI,Lname):
    f=open('poses/'+Lname+'.txt','a')
    f.write('PSO algorithm was performed\n\n\n')
    f.write('The native pose of atoms\n')
    for i in range(0,len(L)):
        for j in range(0,5):
            f.write(str(L[i][j])+'\t')
        f.write('\n')
    for it in range(1,2):
        nop=80
        nob=round(nop/10)
        noi=30
        ls=[]
        CS=first_CS(nop,len(BRA))
        OF=score_population(L,R,B,CS,BRA,BRAI)
        bests=select_bests(OF,nob)
        rm=[]
        rm.append('PSO')
        rm.append(Lname)
        rm.append(str(it))
        for i in range(0,noi):
            move(CS,bests)
            OF=score_population(L,R,B,CS,BRA,BRAI)
            bests=select_bests(OF,nob)
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
