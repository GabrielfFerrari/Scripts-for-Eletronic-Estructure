#!/usr/bin/python3
import matplotlib.pyplot as plt
def DOS_PLOTY():
    print('Calculando DOS')
    x=[]
    y=[]
    data=list()
    DOS=open('name.dos.dat','r')
    for line in DOS:
        if '#' not in line.strip() and '#' not in line.split():
            x.append(float(line.split()[0]))
            y.append(float(line.split()[1]))

    plt.xlabel('$E/eV$', fontsize=16)
    plt.ylabel('DOS (ab. units)', fontsize=16)
    plt.axis([-10, 10, 0, 150])
    plt.annotate('(b)', xy=(10,140), xytext=(10, 150), fontsize=20) # Anotate
    plt.plot(x,y,'k-',linewidth=0.5) # plot
    plt.axvline(x=0, ymin=0, ymax=150,color='c', linestyle='--')
    plt.savefig('name.dos.png', format='png')
def PDOS_PLOTY():
    print('Calculando PDOS')
    collors=[]              # colors for plot, for Atoms
    LABEL=[]                # label of subtitle's for Atoms
    Total_Energy=[[]]    # lista das energias totais
    Total_SpinUp=[[]]    # list of spin1, list of list
    Total_SpinDown=[[]]  # list of spin2, list of list
    PDOS=[open('archive.dat','r')]            #
    plt.xlabel('Energia (eV)', fontsize=18) # legenda eixo x
    plt.ylabel('PDOS (arb. units)', fontsize=18) # legenda eixo y
    plt.axis([-9, 0, -0.55, 0.55]) # xrange e yrange
    for i in range(0,len(PDOS),1): # PDOS plot data
        for line in PDOS[i]:
            if line.strip() !='' and '#' not in line.strip() and '#' not in line.split():
                Total_Energy[i].append(float(line.split()[0]))
                Total_SpinUp[i].append(float(line.split()[1]))
                Total_SpinDown[i].append(-float(line.split()[2]))
        plt.plot(Total_Energy[i],Total_SpinUp[i], collors[i],linewidth=1.75,label=LABEL[i])
        plt.plot(Total_Energy[i],Total_SpinDown[i], collors[i],linewidth=1.75)
    plt.axvline(x=PF, ymin=0, ymax=1,color='c', linestyle='--') # Fermi level in red color
    plt.legend(bbox_to_anchor=(0.99, 0.99), loc='upper left', borderaxespad=0.) # Subtitle for n chemical species
    plt.annotate('(c)', xy=(0,0.55), xytext=(0, 0.55), fontsize=20) # Anotate
    plt.savefig('name.pdos.png', format='png') # save figure
def BANDS_PLOTY():
    print('Calculando estrutura de bandas')
    energyX=list()
    energyY=list()
    bands = open('name.bands.dat','r')
    for line in bands:
        if line.strip() !='' and '#' not in line.split() and '#' not in line.strip():
            energyX.append(float(line.split()[0]))
            energyY.append(float(line.split()[1]))
        if line.strip()=='':
            plt.plot(energyX.copy(),energyY.copy(),'k-',linewidth=0.3)
            energyX.clear()
            energyY.clear()
    plt.annotate('(a)', xy=(0.12,9), xytext=(0.12, 9), fontsize=20) # Anotate
    plt.xlabel('', fontsize=16)
    plt.ylabel('Energia (eV)', fontsize=16)                             # subtitle for x axis
    plt.axis([0, 0.12, -9, 0])                                          # Limits of x and y axis
    plt.axhline(y=PF, xmin=0, xmax=1,color='c', linestyle='--')         # Fermi level in red color
    plt.xticks(( 0,0.12), ('$\Gamma$','$x$'), size=20)                 # Label on x axis, direction on high simmetry
    plt.savefig('name.bands.png', format='png')                              # save figure
def GAP_CALCULATE():
    y = []
    aux = -999
    i=0
    array = open('name.bands.dat', 'r')
    for line in array:
        if line.strip() !='' and '#' not in line.strip() and '#' not in line.split():
            y.append(float(line.split()[1]))
            if float(line.split()[1]) > float(PF) and aux < float(EF):
                print('LUMO:{}  \t HOMO:{} \t GAP: {}'.format(y[i], aux, y[i] - aux))
                break
            aux = float(line.split()[1])
            i+=1
def CONVERGED_CALCULATE():
    constrained = []
    cycle = []
    data = open('conv.dat','r')
    itens = []

    for line in data:
        if line.strip() != '':
            itens.append(line.split()[2])
            constrained.append(float(line.split()[2]))
    cycle = np.arange(0, len(constrained))
    i=len(constrained)
    A=sorted(constrained)
    plt.annotate("Mínimo: "+ str(A[0])  + " eV",  xy=(len(cycle)-8,1.25),xytext=(len(cycle)-8, 1.12),fontsize=12)
    plt.annotate("Máximo: "+ str(A[-1]) + " eV",  xy=(len(cycle)-8,1.25),xytext=(len(cycle)-8, 1.05),fontsize=12)

    for i in range(i-1, i - 40,-1):
        if constrained[i] < 1:
            plt.annotate("0" + itens[i].strip()[0:3], xy=(cycle[i],constrained[i]),xytext=(cycle[i], constrained[i]))
        else:
            plt.annotate(itens[i].strip()[0:3], xy=(cycle[i],constrained[i]),xytext=(cycle[i], constrained[i]))

    plt.axis([len(cycle) - 40,len(cycle),-0.5,1.25])
    plt.axhline(xmin=0, xmax=1000, y=0.05 ,color='r', linestyle='--', linewidth = 0.75)
    plt.plot(cycle,constrained, color='blue', linewidth = 0.5)
    plt.title('file')
    plt.xlabel('Num of Steps', fontsize=16)
    plt.ylabel('EnergyShift ($eV$) ', fontsize=16)
    plt.grid()
    plt.show()    
