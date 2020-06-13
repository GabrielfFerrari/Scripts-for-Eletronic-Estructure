#!/bin/usr/python3
nb=''
xyz_fdf ={}
chemical_species={}
def creatorfdf():
    i=1
    for line in arquivo:
        if line.strip() != '' and nb not in line.split() :
            if line.split()[0] not in chemical_species:
                chemical_species.setdefault(line.split()[0],i)
                i+=1
            arquivo1.write('{0[1]} \t {0[2]} \t {0[3]} \t{1} \t{0[0]}  \n'.format(line.split(), chemical_species[line.split()[0]] ))
for item in xyz_fdf:
    arquivo = open(item,'r')
    arquivo1 = open(xyz_fdf[item],'w')
    cab = open('cabec.txt','r')
    rod = open('rod.txt','r')
    for line0 in cab:
        arquivo1.write(line0)
    cab.close()
    creatorfdf()
    for line1 in rod:
        arquivo1.write(line1)
    rod.close()
    arquivo.close()
    arquivo1.close()
