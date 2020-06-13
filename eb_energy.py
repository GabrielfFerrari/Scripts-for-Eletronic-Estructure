#!/usr/bin/python3
data = open('Tot_enegy.dat','r')
E_mol=-3383.176318
for line in data:
    if '#' not in line.split():
        for i in range(1,4,1):
           print( -(float(line.split()[i]) - float(line.split()[0]) - E_mol))
        print(50*'*')
