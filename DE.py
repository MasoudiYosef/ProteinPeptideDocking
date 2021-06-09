from first_CS import first_CS
from base_parameters import RMSD
from score import score_population
from score import change_Ligand
from Trader import select_bests
import numpy as np
import copy
      

def Update_Cs(CS,L,R,B,BRA,BRAI,bests,OF):
    for i in range(0,len(CS)):
        a=np.random.randint(len(CS))
        b=np.random.randint(len(CS))
        c=np.random.randint(len(CS))
        C=np.zeros([1,len(CS[0])])
        if i != round(bests[0][0]):
            for j in range(0,len(CS[0])):
                cr=np.random.rand()
                f=0.8
                if cr>=0.1:
                    if j<3:
                        r=np.random.randint(20)
                        C[0][j]=CS[a][j]+(CS[b][j]-CS[c][j])*r
                    else:
                        r=np.random.randint(50)
                        C[0][j]=CS[a][j]+f*(CS[b][j]-CS[c][j])*r
            F=score_population(L,R,B,C,BRA,BRAI)
            co=0
            for m in range(0,4):
                if F[0][m]<OF[i][m]:
                    co=co+1
            if co>2:
                CS[i]=C
                OF[i]=F
                

def DE(L,R,B,BRA,BRAI,Lname):
    f=open('poses/'+Lname+'.txt','a')
    f.write('DE algorithm was performed\n\n\n')
    f.write('The native pose of atoms\n')
    for i in range(0,len(L)):
        for j in range(0,5):
            f.write(str(L[i][j])+'\t')
        f.write('\n')
    for it in range(1,2):
        nop=50
        nob=1
        noi=3
        ls=[]
        CS=first_CS(nop,len(BRA))
        OF=score_population(L,R,B,CS,BRA,BRAI)
        bests=select_bests(OF,nob)
        rm=[]
        rm.append('DE')
        rm.append(Lname)
        rm.append(str(it))
        for i in range(0,noi):
            Update_Cs(CS,L,R,B,BRA,BRAI,bests,OF)
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
