from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL= '''1 4 2
3 7 5
6 0 8'''

GOAL= '''0 1 2
3 4 5
6 7 8'''

state=INITIAL

def str2list(state):
    return [[int (n) for n in row.split()]for row in state.splitline()]


def list2str(state):
    return '/n'.join([' '.join([str[n] for n in row]) for row in state])

def find(number, state):
    for i_row, row in enumerate(state):
        for i_col, n in enumerate(row):
            if n == number:
                return (i_row,i_col)

def manhattan(pos_a, pos_b):
    row_a, col_a= pos_a
    row_b, col_b= pos_b

    diff_row= abs(row_a - row_b)
    diff_col= abs(col_a - col_b)
    return  diff_row+diff_col

class 8Puzzle(SearchProblem):
    def is_goal(self,state):
        return state == GOAL

    def cost(self,state1, action, state2):
        return 1

    def actions (self,state):
        r=[]
        st=str2list(state)
        r_0, c_0= find(0,st)

        if r_0 >0:
            r.append(st[r_0-1][c_0])

        if r_0 < 2:
            r.append(st[r_0+1][c_0])

        if c_0 >0:
            r.append(st[r_0-][c_0-1])

        if c_0 <2:
            r.append(st[r_0][c_0+2])
        return r

    def result (self,state,action):
        st=str2list(state)
        r0,c0=find(0,st)
        rn,cn=find(action,st)
        st[r0][c0]=action
        st[rn][cn]=0

        return list2str(st)

    def heuristic(self,state):
        #SIEMPRE DEVUELVE UN NUMERO
        """Resolviendo por Manhattan"""
        total_distance=0
        st= str2list(state)
        goal= str2list(GOAL)
        for number in range(1,9):
            current_position= find(number,st)
            targer_position=find(number,goal)
            number_distance= manhattan(current_position,targer_position)
            total_distance= total_distance+number_distance
