import MDAnalysis as mda
import numpy as np
import pytim 
from pytim.datafiles import *

u       = mda.Universe(WATER_GRO,WATER_GRO)
oxygens = u.select_atoms("name OW") 
radii=pytim_data.vdwradii(G43A1_TOP)

interface = pytim.ITIM(u,alpha=2.,itim_group=oxygens,max_layers=4)#,multiproc=True,radii_dict=radii,cluster_groups=oxygens,cluster_cut=3.5)
interface.lap()
interface.assign_layers()
interface.lap()

layer = interface.layers('upper',1)  # first layer
print ("Interface computed. Upper layer:\n %s out of %s" % (layer,oxygens))

interface.writepdb('layers.pdb')

