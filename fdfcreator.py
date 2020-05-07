#!/bin/usr/python3
nb='128'
xyz_fdf ={'int1_cob55.xyz':'int1_cob55.fdf','int2_cob55.xyz':'int2_cob55.fdf','int3_cob55.xyz':'int3_cob55.fdf'}
chemical_species={}
def creatorfdf():
    i=1
    for line in arquivo:
        if line.strip() != '' and nb not in line.strip() :
            if line.split()[0] not in chemical_species:
                chemical_species.setdefault(line.split()[0],i)
                i+=1
            arquivo1.write('{0[1]} \t {0[2]} \t {0[3]} \t{1} \t{0[0]}  \n'.format(line.split(), chemical_species[line.split()[0]] ))


cab = open('cabec.txt','r')
rod = open('rod.txt','r')
for item in xyz_fdf:
    arquivo = open(item,'r')
    arquivo1 = open(xyz_fdf[item],'w')
    for line0 in cab:
        arquivo1.write(line0)
    creatorfdf()   
    for line1 in rod:
        arquivo1.write(line1)
    arquivo.close()
    arquivo1.close()
