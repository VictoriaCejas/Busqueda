'''Numero es la casilla en donde estoy parado: 0 o 1
la lista representa si esta limpia o no la casilla
True significa sucio
False significa limpio
s=estado
a=accion

Todo lo que vaya a cambiar en el mundo va a estar dentro del estado.
'''
#aspiradora
estado_inicial=(0,[True,True])

def actions(s):
        return['L','R','S']
        #en este caso son las mismas acciones, si no hay que buscarlas.
        #acciones que estan disponibles
def result(s,a):
    pos,mugres= S
    if a == 'S':
        mugres[pos]=False
    elif a=="L"
        pos=0
    else
        pos=1
    return (pos,mugres)
    #estado en que queda realizando una accion.

def is_goal(s):
    return not any(S[1])

def cost(s,a,s2):
    return 1
