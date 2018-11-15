#!/usr/bin/env python3

# Minimize a pdb file, return a pdb and a topologie

__author__ = "Samuel Murail"


import gromacs.gmx5 as gmx
import argparse
from glob import glob
import os

# Parse arguments :
parser = argparse.ArgumentParser(description="Minimize a pdb structure")
parser.add_argument('-fsys', action="store", dest="f_sys", help='Input PDB file of the system')
parser.add_argument('-psys', action="store", dest="p_sys", help='Topologie in gromacs format .top of the system')
parser.add_argument('-fmol', action="store", dest="f_mol", help='Input PDB file of the molecule to insert')
parser.add_argument('-pmol', action="store", dest="p_mol", help='Topologie in gromacs format .top of the molecule to insert')
parser.add_argument('-nmol', action="store", dest="num_mol", help='Number of molecule to insert', type=int, default=20)
parser.add_argument('-o', action="store", dest="o", help='Output Directory')
parser.add_argument('-n', action="store", dest="name", help='Output file name')
args = parser.parse_args()




#print("Min steps :\t",args.min_steps,"\nEqui HA time :",args.HA_time,"ns\nEqui CA time :",args.CA_time,"ns\nEqui CA_LOW time :",args.CA_LOW_time,"ns")

sys_raw = gmx.GmxSys(name = args.name, coor_file = args.f_sys, top_file = args.p_sys)
mol_gmx = gmx.GmxSys(name = "mol", coor_file = args.f_mol, top_file = args.p_mol)

sys_raw.display()
mol_gmx.display()

sys_raw.insert_mol_sys(mol_gromacs=mol_gmx, mol_num=args.num_mol, new_name=args.name, out_folder=args.o, check_file_out = True)
#	mol_num = args.num_mol, mol_length = 3, out_folder = args.o, sys_name = args.name)

#insert_mol_sys(self, mol_gromacs, mol_num, new_name, out_folder, check_file_out = True):
        

### TO DO ####
print("\n\nInsertion was sucessfull \n\tSystem directory :\t"+args.o+"\n\tsystem coor file:\t"+sys_raw.coor_file+"\n\tsystem top file:\t"+sys_raw.top_file)

#~/Documents/repository/Gromacs_Setup/insert_mol.py 
#-fsys mini_equi_3_step_SOL_ION_2cyh/03_equi_CA_LOW/equi_CA_LOW_2cyh_compact.gro 
#-psys solv_ion_2cyh/solv_ion_2cyh.top 
#-fmol ARP/01_equi_imp/equi_implicit_compact.gro 
#-pmol ARP/ARP_pdb2gmx.top 
#-nmol 20 -o 2CYH_20_ARP -n 2cyh_20_ARP