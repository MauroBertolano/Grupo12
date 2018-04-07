import random
laberintoDiseño=[[False,True,False,True,False,False],
           [False,True,False,False,False,True],
           [False,False,False,True,False,False],
           [True,False,True,True,False,False],
           [True,False,True,True,False,True],
           [True,False,False,True,False,False]]

def laberinto(lab,iniX,iniY,finX,finY):
    if(lab[iniX][iniY]==True or lab[finX][finY]==True):
        return print('El inicio o final se encuentra en una pared')
    if(iniX==finX and iniY==finY):
        return print('Se encontró la salida')
    var=0
    while (var==0):
        x=random.randint(1,4)
        '''1: derecha, 2: arriba, 3:izquierda, 4:abajo'''
        if(x==1 and 5>=iniX>=0 and 5>=iniY+1>=0):
            if(lab[iniX][iniY+1]==False):
                laberinto(lab,iniX,iniY+1,finX,finY)
                return
        elif (x==2 and 5>=iniX-1>=0 and 5>=iniY>=0):
            if(lab[iniX-1][iniY]==False):
                laberinto(lab,iniX-1,iniY,finX,finY)
                return
        elif (x==3 and 5>=iniX>=0 and 5>=iniY-1>=0):
            if(lab[iniX][iniY-1]==False):
                laberinto(lab,iniX,iniY-1,finX,finY)
                return
        elif (x==4 and 5>=iniX+1>=0 and 5>=iniY>=0):
            if(lab[iniX+1][iniY]==False):
                laberinto(lab,iniX+1,iniY,finX,finY)
                return

laberinto(laberintoDiseño,0,0,5,5)
