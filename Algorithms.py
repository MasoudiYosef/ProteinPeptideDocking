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
LList=['1b9j','2oy2','3gq1','3bs4','2oxw','2b6n','1tw6','3vqg','1uop','4c2c','4j44','2hpl','2v3s','3nfk','1nvr','4v3i','3t6r','1svz','3d1e','3idg','3lny','4nnm','4q6h','3mmg','3q47','3upv','4qbr','3njg','1elw','3ch8','4wlb','1ou8','1n7f','3obq','4btb','2w0z','4n7h','2qab','1h6w','3brl','1ntv','4ds1','2o02','1n12','2xfx','3bfw','4eik','3ds1','4j8s','2w10','3jzo','4dgy','2b9h']
i=14
Algorithm='Trader'
Lpath='Dataset/Ligands/L-'+LList[i]+'.pdbqt'
Rpath='Dataset/Receptors/'+LList[i]+'/R_'+LList[i]+'.pdbqt'
Lig=get_ligand(Lpath)
Receptor=get_ligand(Rpath)
root=get_root(Lpath)
branches,serials=get_branch(Lpath)
if Algorithm=='Trader':
    Trader(Lig,Receptor,base,branches,serials,LList[i])
if Algorithm=='DE':
    DE(Lig,Receptor,base,branches,serials,LList[i])
if Algorithm=='PSO':
    PSO(Lig,Receptor,base,branches,serials,LList[i])
if Algorithm=='GA':
    GA(Lig,Receptor,base,branches,serials,LList[i])
