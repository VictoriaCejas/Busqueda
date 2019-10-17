import
#(c3,c5) tupla con la cantidad de litros de cada jarra (lts jarra 3, lts jarra 4)
#c_max= capacidades maximas de las jarras, solo usar constantes como globales, si no, el arbol se rompe
# la solucion es que la jarra de 5 tenga 4 lts. y la de 3 0 lts.
inicial=(0,0)
c_max=(3,5)

def is_goal(state):
    c3,c5= state
    return c5 == 4

def cost(state, action, stateChild):
    return 1

def actions(state):
    act=[]
    c3,c5 = state
    if c5 > 0:
        act.append(('vaciar',1)) #1 es la posicion de la jarra 5 en la tupla
    if c3 > 0:
        act.append(('vaciar',0)) #0 es la posicion de la jarra 3 en la tupla
    if c5 < 5
        act.append(('llenar',1))
    if c3 < 5
        act.append(('llenar',0))
    if c5>0 and c3 < 3:
        act.append(('tras',1)) #pasar de la 5 a la 3
    if c3>0 and c5 < 5:
        act.append(('tras',0)) #pasar de la 3 a la 5
    return act

def result(self, state, actions):
    c3,c5= state
    accion,origen= actions
    new_st=[c3,c5]
    if accion =='vaciar':
        new_st[origen]=0
    elif accion == 'llenar':
        new_st[origen]=c_max[origen]
    else accion= 'tras':
        destino=0 if origen=1 else 1
        puedepasar= new_st[origen]
        puederecibir=c_max[destino] - new_st[destino]
        apasar= min(puedepasar, puederecibir)
        new_st[origen] - = apasar
        new_st[destino]+ =apasar
    return tuple(new_st)
