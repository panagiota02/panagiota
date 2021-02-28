import math
import random
def gemisma_pinaka(tetrag,diast):
    arithmos_theseon=diast*diast
    no_monadon= math.ceil((arithmos_theseon)/2)
    for i in range(diast):
        for j in range(diast):
            tetrag[i][j]=10
    x=random.randint(0,diast-1)
    y=random.randint(0,diast-1)
    cnt=0
    while cnt<no_monadon :
            if tetrag[x][y] == 10:
                tetrag[x][y]=random.randint(0,9)
                cnt+=1
            x=random.randint(0,diast-1)
            y=random.randint(0,diast-1)
            
def paroysiasi_pinaka (tetrag,diast):
    for i in range(diast):
        for j in range(diast):
             print("%5s"%(int(tetrag[i][j])), end=" ")
        print("\n")
        
def check_orizontia (tetrag, diast): #gia oles tis sires
    cnt=0
    for i in range (0,diast):   #gia kathe sira
        for i1 in range (0,diast-3):
           vrika_tetrada=True
           for i2 in range(i1,i1+4):
                if (tetrag[i][i2]//10 != 0):
                    vrika_tetrada=False
           if vrika_tetrada == True:
              cnt+=1
    return cnt

def check_katheta (tetrag, diast): #gia oles tis stiles
    cnt=0
    for j in range (0,diast):   #gia kathe stili
        for j1 in range (0,diast-3):
           vrika_tetrada=True
           for j2 in range(j1,j1+4):
                if (tetrag[j2][j]//10 != 0):
                    vrika_tetrada=False
           if vrika_tetrada == True:
              cnt+=1
    return cnt     
    
def diakonies_pinaka (tetrag, diast): # diagonio -> \ diagonio -> /
    cnt=0
    for sira in range(0,diast-3):
        for stili in range(0,diast-3):
            if sira==stili:         #diagonios1
                    vrika_tetrada=True
                    for s in range(sira,sira+4):
                        if (tetrag[s][s]//10 != 0):
                            vrika_tetrada=False
                    if vrika_tetrada == True:
                        cnt+=1

            if sira+stili== diast-1: #diagonios2
                    x=stili
                    vrika_tetrada=True
                    for s in range(sira,sira+4):
                        if (tetrag[s][x]//10 != 0):
                            vrika_tetrada=False
                        x-=1
                    if vrika_tetrada == True:
                        cnt+=1
    return cnt 
    
def diakonia_kato (tetrag, diast): #diagonia -> \
    cnt=0
    z=diast-3
    for sira in range(1,z):
        x=0
        for i in range(sira,z):           
            vrika_tetrada=True
            w=x
            for d in range(i,i+4):
                if (tetrag[d][w]//10 != 0):
                   vrika_tetrada=False
                w+=1
            if vrika_tetrada == True:
                        cnt+=1
            x+=1
    return cnt

def diakonia_pano(tetrag, diast): #diagonia -> \
    cnt=0
    z=diast-3
    for stili in range(1,z):
            x=0
            for j in range(stili,z):
                vrika_tetrada=True
                w=x
                for d in range(j,j+4):
                   if (tetrag[w][d]//10 != 0):
                        vrika_tetrada=False
                   w+=1
                if vrika_tetrada == True:
                        cnt+=1
                x+=1
                
    return cnt

def diakonia_aristera(tetrag, diast): #diagonia -> /
    cnt=0
    a=diast-2
    z=2
    for stili in range(a,z,-1):
        x=0
        for j in range(stili,z,-1):
              vrika_tetrada=True
              w=x
              for d in range(j,j-4,-1):
                 if (tetrag[w][d]//10 != 0):
                      vrika_tetrada=False
                 w+=1
              if vrika_tetrada == True:
                      cnt+=1
              x+=1
                
    return cnt
        
def diakonia_deksia(tetrag, diast): #diagonia -> /
    cnt=0
    z=diast-3    
    for stili in range(1,z):
            x=diast-1
            for j in range(stili,z):
                vrika_tetrada=True
                w=x
                for d in range(j,j+4):
                   if (tetrag[w][d]//10 != 0):
                        vrika_tetrada=False
                   w-=1
                if vrika_tetrada == True:
                        cnt+=1
                x-=1
                
    return cnt

           
diastasi= int(input("Dose diastasi tetragonou: "))
tetragono=[[10 for i in range(diastasi)] for j in range(diastasi)]
total=0
for i in range(0,100):
    gemisma_pinaka(tetragono,diastasi)
    a=check_orizontia(tetragono,diastasi)
    b=check_katheta(tetragono,diastasi)
    c=diakonies_pinaka(tetragono,diastasi)
    d=diakonia_kato(tetragono,diastasi)
    e=diakonia_pano(tetragono,diastasi)
    f=diakonia_aristera(tetragono,diastasi)
    g=diakonia_deksia(tetragono,diastasi)
    total=total+a+b+c+d+e+f+g
#   paroysiasi_pinaka(tetragono,diastasi)
#   print()
print("Sinolikos arithmos tetradon : " + str(total))
print("Mesos oros tetradon : " + "%4.2f%1s"%(total/100,"%"))

