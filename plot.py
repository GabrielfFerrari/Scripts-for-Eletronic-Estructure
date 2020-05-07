import pandas as pd 
import matplotlib.pyplot as plt
colum1=[]
colum2=[]
colum3=[]
colum4=[]
vallence=[]
def charges(): # Plot of PSEUDO AND ALL ELECTRONS CHARGE
    label = ['AE Core Charge','PS Core Charge']
    labelps = ['AE Vallence Charge', 'PS Vallence Charge']
    i=0
    plt.axis([0,3,0,14])
    data = [open('AECHARGE','r'),open('PSCHARGE','r')]
    for item in data:
        for line in item:
            colum1.append(float(line.split()[0])) # radius
            colum4.append(float(line.split()[3])) # core charge 
            if i==0:
                vallence.append(float(line.split()[1]) + float(line.split()[2]) - float(line.split()[3])) # vallence total charge for all electrons
            if i==1:
                vallence.append(float(line.split()[1]) + float(line.split()[2]) ) # vallence total charge for PSEUDOCHARGE
        i+=1    
        plt.plot(colum1.copy(), colum4.copy(),linewidth = 1.0, label = label[i-1])
        plt.plot(colum1.copy(), vallence.copy(),linewidth = 1.0, label = labelps[i-1])
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.)
        colum1.clear()
        colum4.clear()
        vallence.clear()
    plt.xlabel('r (au)', fontsize=16)
    plt.ylabel('$rho * r^{2} (arb.units)$', fontsize=16)
    plt.show()


def ionic_potential(): # Plot for ionic pseudopotential
    data=[open('PSPOTR0','r'), open('PSPOTR1','r'), open('PSPOTR2','r'), open('PSPOTR3','r') ] 
    label = ['$V_{s}$','$V_{p}$','$V_{d}$','$V_{f}$']
    plt.axis([0,4,-2,3])
    i=0
    for item in data:
        for line in item:
            colum1.append(float(line.split()[0])) # radius 
            colum2.append(float(line.split()[1])) # s,p,d or f vallence orbitals
        plt.plot(colum1.copy(), colum2.copy(),linewidth = 1.0, label = label[i])       
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.)
        i+=1
        colum1.clear()
        colum2.clear()
        plt.ylabel('$V(Ry)$',fontsize=16)
        plt.xlabel('$r(au)$',fontsize=16)
    plt.show()
ionic_potential()
