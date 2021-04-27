from first_CS import first_CS
from base_parameters import RMSD
from score import score_population
from score import change_Ligand
import numpy as np
import copy


def select_bests(OF,nog):
    bests=np.zeros([nog,2])
    do=np.zeros([len(OF),1])
    for i in range(0,len(OF)):
        for j in range(0,len(OF)):
            for m in range(0,4):
                if (OF[i][m]>=OF[j][m]):
                    do[i][0]=do[i][0]+1
    for i in range(0,nog):
        mi=do[0][0]
        k=0
        for j in range(1,len(OF)):
            if do[j][0]<mi:
                mi=do[j][0]
                k=j
        bests[i][0]=k
        bests[i][1]=do[k][0]
        OF=np.delete(OF,k,0)
        do=np.delete(do,k,0)
    for i in range(nog-1,-1,-1):
        c=0
        for j in range(0,i):
            if bests[j][0]<bests[i][0]:
                c=c+1
        bests[i][0]=bests[i][0]+c
    return bests
    
            

def grouping(OF):
    c=len(OF)
    nog=round(c/5)
    groups=np.zeros([c,1])
    bests=select_bests(copy.deepcopy(OF),nog)
    s=0
    for i in range(0,len(bests)):
        s=s+bests[i][1]
        groups[round(bests[i][0])][0]=bests[i][0]
    s1=0
    for i in range(0,len(bests)):
        if bests[i][1]==0:
            bests[i][1]=1
        bests[i][1]=s/bests[i][1]
        s1=s1+bests[i][1]
    ls=[]
    for i in range(0,len(bests)):
        k=round(c*bests[i][1]/s1)
        for j in range(0,k):
            ls.append(bests[i][0])
    for i in range(1,c):
        k=np.random.randint(len(ls))
        if groups[i][0]==0:
            v=ls[k]
            groups[i][0]=v
            ls.remove(v)
            if len(ls)<=0:
                break
    return groups,bests
    

def distributing(CS,OF,groups,L,R,B,BRA,BRAI):
    for i in range(0,len(CS)):
        if i!=groups[i][0]:
            d=round(groups[i][0])
            k=np.random.randint(round(len(CS[0])/5))
            C=np.zeros([1,len(CS[0])])
            C[0]=CS[i]
            for j in range(0,k):
                r=np.random.randint(len(CS[0]))
                C[0][r]=CS[d][r]
            F=score_population(L,R,B,C,BRA,BRAI)
            c=0
            for m in range(0,4):
                if F[0][m]<OF[i][m]:
                    c=c+1
            if c>2:
                CS[i]=C
                OF[i]=F


def retailing(CS,OF,groups,L,R,B,BRA,BRAI):
    for i in range(0,len(CS)):
        k=np.random.randint(round(len(CS[0])/5))
        C=np.zeros([1,len(CS[0])])
        C[0]=CS[i]
        for j in range(0,k):
            r=np.random.randint(len(CS[0]))
            m=np.random.randint(2)
            f=-1
            if m==1:
                f=1
            if r<3:
                l=-C[0][r]
                h=C[0][r]
                C[0][r]=C[0][r]+f*np.random.uniform(low=l, high=h, size=(1,))[0]
            else:
                h=max(C[0][r],2)
                C[0][r]=C[0][r]+f*np.random.randint(round(h))
        F=score_population(L,R,B,C,BRA,BRAI)
        c=0
        for m in range(0,4):
            if F[0][m]<OF[i][m]:
                c=c+1
        if c>2:
            CS[i]=C
            OF[i]=F


def new_retailing(CS,L,R,B,BRA,BRAI,OF,bests):
        for i in range(0,len(CS)):
            a=np.random.randint(len(CS))
            b=np.random.randint(len(CS))
            c=np.random.randint(len(CS))
            C=np.zeros([1,len(CS[0])])
            if i != round(bests[0][0]):
                for j in range(0,len(CS[0])):
                    cr=np.random.rand()
                    f=0.8
                    if cr>=0.3:
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


def importing_exporting(CS,OF,groups,bests,L,R,B,BRA,BRAI):
    for i in range(0,len(bests)):
        d=round(bests[i][0])
        k=np.random.randint(len(CS[0])/5)
        C=np.zeros([1,len(CS[0])])
        C[0]=CS[d]
        for j in range(0,k):
            r=np.random.randint(len(CS[0]))
            m=np.random.randint(len(bests))
            C[0][r]=CS[m][r]
        F=score_population(L,R,B,C,BRA,BRAI)
        c=0
        for m in range(0,4):
            if F[0][m]<OF[i][m]:
                c=c+1
        if c>2:
            CS[i]=C
            OF[i]=F


def Trader(L,R,B,BRA,BRAI,Lname):
    for it in range(1,11):
        noc=30
        noi=30
        ls=[]
        CS=first_CS(noc,len(BRA))
        OF=score_population(L,R,B,CS,BRA,BRAI)
        groups,bests=grouping(OF)
        rm=[]
        rm.append('TR')
        rm.append(Lname)
        rm.append(str(it))
        for i in range(0,noi):
            distributing(CS,OF,groups,L,R,B,BRA,BRAI)
            if i%2==0:
                retailing(CS,OF,groups,L,R,B,BRA,BRAI)
            else:
                new_retailing(CS,L,R,B,BRA,BRAI,OF,bests)
            importing_exporting(CS,OF,groups,bests,L,R,B,BRA,BRAI)
            groups,bests=grouping(OF)
            ls.append(OF[round(bests[0][0])])
            s=round(bests[0][0])
            Lig=change_Ligand(CS[s],copy.deepcopy(L),BRA,BRAI)
            rmsd=RMSD(L,Lig)
            rm.append(str(rmsd))
        for j in range(0,4):
            for i in range(0,len(ls)):
                rm.append(ls[i][j])
        f=open('results.txt','a')
        f.write(str(rm)+"\n")
        f.close()
        O=[]
        O.append('TR')
        O.append(Lname)
        O.append(str(it))
        for i in range(0,len(OF)):
            for j in range(0,len(OF[0])):
                O.append(str(OF[i][j]))
        fo=open('MO.txt','a')
        fo.write(str(O)+"\n")
        fo.close()
