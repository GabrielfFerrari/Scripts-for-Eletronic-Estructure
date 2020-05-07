#!/usr/bin/python3
E_tubos =[-18552.887184]
E_molecula =-3383.174867 #real number
E_merge =[-21936.049792]
Eb=list()
i=0

while i < len(E_tubos): # trocar o #k pela quantidade de compostos do sistema
    Eb.append(E_merge[i] - E_tubos[i] - E_molecula )
    print('Energia de ligação do sistema {} é: {}'.format(i + 1, Eb[i]))
    i+=1

