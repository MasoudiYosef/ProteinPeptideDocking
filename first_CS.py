def first_CS(noc,B):
    import numpy as np
    positions=np.random.randint(20,size=(noc,3))+np.random.rand(noc,3)
    ligand_branches=np.random.randint(50,size=(noc,B))
    first_p=np.hstack((positions,ligand_branches))
    return first_p
