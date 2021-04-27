f=open('base.txt','r')
base=[]
l=f.readline()
while len(l)>0:
    l=l.replace('\n','')
    l=l.replace("'",'')
    l=l.split(',')
    base.append(l)
    l=f.readline()
from score import score
import numpy as np
import copy
from math import *
from base_parameters import get_ligand
from base_parameters import get_root
from base_parameters import get_branch
from base_parameters import set_ligand
from base_parameters import RMSD
from Trader import Trader
from GA import GA
from PSO import PSO
from DE import DE
LList=['1b9j','2oy2','3gq1','3bs4','2oxw','2b6n','1tw6','3qg','1uop','4c2c','4j44','2hpl','2v3s','3nfk','1nr','4v3i','3t6r','1svz','3d1e','3idg','3lny','4nnm','4q6h','3mmg','3q47','3up','4qbr','3njg','1elw','3ch8','4wlb','1ou8','1n7f','3obq','4btb','2w0z','4n7h','2qab','1h6w','3brl','1ntv','4ds1','2o02','1n12','2xfx','3bfw','4eik','3ds1','4j8s','2w10','3jzo','4dgy','2b9h']
for i in range(0,53):
    Lpath='Dataset/pdbqt/L-'+LList[i]+'.pdbqt'
    Rpath='Dataset/Receptors/'+LList[i]+'/R_'+LList[i]+'.pdbqt'
    Ligand=get_ligand(Lpath)
    Lig=set_ligand(copy.deepcopy(Ligand))
    Receptor=get_ligand(Rpath)
    root=get_root(Lpath)
    branches,serials=get_branch(Lpath)
    Trader(Lig,Receptor,base,branches,serials,LList[i])
    DE(Lig,Receptor,base,branches,serials,LList[i])
    PSO(Lig,Receptor,base,branches,serials,LList[i])
    GA(Lig,Receptor,base,branches,serials,LList[i])
