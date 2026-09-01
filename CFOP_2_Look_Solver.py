import itertools
from Base_Cube_Processor import *





def SolveCross(scramble: list):
    crossEdges = [(46,43), (48,34), (50,16), (52,25)]
    sol = []
    working_scramble = scramble.copy()
    stickers = [46,48,50,52]

    while len(sol) < 100 and numsolved(working_scramble,stickers) < 4:
        nextsol = ()
        num = numsolved(working_scramble,stickers)
        testing_scramble = working_scramble.copy()
        for c in itertools.product(Moves, repeat=1):
            for i in c:
                testing_scramble = compose(testing_scramble,i)
            if numsolved(testing_scramble,stickers) > num:
                num = numsolved(testing_scramble,stickers)
                nextsol = c
                break
            testing_scramble = working_scramble.copy()
        else:
            for c in itertools.product(Moves, repeat=2):
                for i in c:
                    testing_scramble = compose(testing_scramble,i)
                if numsolved(testing_scramble,stickers) > num:
                    num = numsolved(testing_scramble,stickers)
                    nextsol = c
                    break
                testing_scramble = working_scramble.copy()
            else:
                for c in itertools.product(Moves, repeat=3):
                    for i in c:
                        testing_scramble = compose(testing_scramble,i)
                    if numsolved(testing_scramble,stickers) > num:
                        num = numsolved(testing_scramble,stickers)
                        nextsol = c
                        break
                    testing_scramble = working_scramble.copy()
                else:
                    for c in itertools.product(Moves, repeat=4):
                        for i in c:
                            testing_scramble = compose(testing_scramble,i)
                        if numsolved(testing_scramble,stickers) > num:
                            num = numsolved(testing_scramble,stickers)
                            nextsol = c
                            break
                        testing_scramble = working_scramble.copy()
                    else:
                        nextsol = R

        for l in nextsol:
            working_scramble = compose(working_scramble,l)

            if l == R:
                sol.append("R")
            if l == L:
                sol.append("L")
            if l == U:
                sol.append("U")
            if l == D:
                sol.append("D")
            if l == F:
                sol.append("F")
            if l == B:
                sol.append("B")
            if l == Ri:
                sol.append("Ri")
            if l == Li:
                sol.append("Li")
            if l == Ui:
                sol.append("Ui")
            if l == Di:
                sol.append("Di")
            if l == Fi:
                sol.append("Fi")
            if l == Bi:
                sol.append("Bi")
            if l == R2:
                sol.append("R2")
            if l == L2:
                sol.append("L2")
            if l == U2:
                sol.append("U2")
            if l == D2:
                sol.append("D2")
            if l == F2:
                sol.append("F2")
            if l == B2:
                sol.append("B2")
    return sol


def F2Lnumsolved(scramble: list):#Checks how many stickers are solved
    F2Lpairs = [(45,42,35,39,32), (47,44,15,41,12), (51,26,33,23,30), (53,24,17,21,14)]
    
    num = 0
    for c in F2Lpairs:
        if scramble[c[0]] == c[0] and scramble[c[3]] == c[3]:
            num = num+1
    return num

def F2Lsquisher(moves: tuple):
    sol = []
    for l in moves:
        if l == R:
            sol.append("R")
            endmove = "Ri"
        if l == L:
            sol.append("L")
            endmove = "Li"
        if l == U:
            sol.append("U")
        if l == F:
            sol.append("F")
            endmove = "Fi"
        if l == B:
            sol.append("B")
            endmove = "Bi"
        if l == Ri:
            sol.append("Ri")
            endmove = "R"
        if l == Li:
            sol.append("Li")
            endmove = "L"
        if l == Ui:
            sol.append("Ui")
        if l == Fi:
            sol.append("Fi")
            endmove = "F"
        if l == Bi:
            sol.append("Bi")
            endmove = "B"
        if l == U2:
            sol.append("U2")
    sol.append(endmove)

    return (convert(sol),sol)

def SolveF2L(scramble: list):
    slotMoves = [R, Ri, L, Li, F, Fi, B, Bi]
    upMoves = [U, Ui, U2]
    idUpMoves = [I,U,Ui,U2]
    F2LMoves = itertools.product(slotMoves,upMoves)
    sol = []
    working_scramble = scramble.copy()

    while len(sol) < 100 and F2Lnumsolved(working_scramble) < 4:
        nextsol = ()
        nextappend = []
        num = F2Lnumsolved(working_scramble)
        testing_scramble = working_scramble.copy()
        for c in F2LMoves:
            testing_scramble = compose(testing_scramble,F2Lsquisher(c)[0])
            if F2Lnumsolved(testing_scramble) > num:
                num = F2Lnumsolved(testing_scramble)
                nextsol = F2Lsquisher(c)[0]
                nextappend = F2Lsquisher(c)[1]
                break
            testing_scramble = working_scramble.copy()
        else:
            for c in itertools.product(idUpMoves, slotMoves, upMoves):
                testing_scramble = compose(testing_scramble,c[0])
                testing_scramble = compose(testing_scramble,F2Lsquisher((c[1],c[2]))[0])
                if F2Lnumsolved(testing_scramble) > num:
                    num = F2Lnumsolved(testing_scramble)
                    nextsol = compose(c[0],F2Lsquisher((c[1],c[2]))[0])
                    if c[0] == U:
                        nextappend.append("U")
                    if c[0] == Ui:
                        nextappend.append("Ui")
                    if c[0] == U2:
                        nextappend.append("U2")
                    nextappend = nextappend + F2Lsquisher((c[1],c[2]))[1]
                    break
                testing_scramble = working_scramble.copy()
            else:
                for c in itertools.product(slotMoves, upMoves, idUpMoves, slotMoves, upMoves):
                    testing_scramble = compose(testing_scramble,F2Lsquisher((c[0],c[1]))[0])
                    testing_scramble = compose(testing_scramble,c[2])
                    testing_scramble = compose(testing_scramble,F2Lsquisher((c[3],c[4]))[0])
                    if F2Lnumsolved(testing_scramble) > num:
                        num = F2Lnumsolved(testing_scramble)
                        nextsol = compose(F2Lsquisher((c[0],c[1]))[0],compose(c[2],F2Lsquisher((c[3],c[4]))[0]))
                        nextappend = nextappend + F2Lsquisher((c[0],c[1]))[1]
                        if c[2] == U:
                            nextappend.append("U")
                        if c[2] == Ui:
                            nextappend.append("Ui")
                        if c[2] == U2:
                            nextappend.append("U2")
                        nextappend = nextappend + F2Lsquisher((c[3],c[4]))[1]
                        break
                    testing_scramble = working_scramble.copy()
                else:
                    for c in itertools.product(idUpMoves, slotMoves, upMoves, idUpMoves, slotMoves, upMoves):
                        testing_scramble = compose(testing_scramble,c[0])
                        testing_scramble = compose(testing_scramble,F2Lsquisher((c[1],c[2]))[0])
                        testing_scramble = compose(testing_scramble,c[3])
                        testing_scramble = compose(testing_scramble,F2Lsquisher((c[4],c[5]))[0])
                        if F2Lnumsolved(testing_scramble) > num:
                            num = F2Lnumsolved(testing_scramble)
                            nextsol = compose(c[0],compose(F2Lsquisher((c[1],c[2]))[0],compose(c[3],F2Lsquisher((c[4],c[5]))[0])))
                            if c[0] == U:
                                nextappend.append("U")
                            if c[0] == Ui:
                                nextappend.append("Ui")
                            if c[0] == U2:
                                nextappend.append("U2")
                            nextappend = nextappend + F2Lsquisher((c[1],c[2]))[1]
                            if c[3] == U:
                                nextappend.append("U")
                            if c[3] == Ui:
                                nextappend.append("Ui")
                            if c[3] == U2:
                                nextappend.append("U2")
                            nextappend = nextappend + F2Lsquisher((c[4],c[5]))[1]
                            break
                        testing_scramble = working_scramble.copy()
                    else:
                        for c in itertools.product(slotMoves, upMoves, idUpMoves, slotMoves, upMoves, idUpMoves, slotMoves, upMoves):
                            testing_scramble = compose(testing_scramble,F2Lsquisher((c[0],c[1]))[0])
                            testing_scramble = compose(testing_scramble,c[2])
                            testing_scramble = compose(testing_scramble,F2Lsquisher((c[3],c[4]))[0])
                            testing_scramble = compose(testing_scramble,c[5])
                            testing_scramble = compose(testing_scramble,F2Lsquisher((c[6],c[7]))[0])
                            if F2Lnumsolved(testing_scramble) > num:
                                num = F2Lnumsolved(testing_scramble)
                                nextsol = compose(F2Lsquisher((c[0],c[1]))[0],compose(c[2],compose(F2Lsquisher((c[3],c[4]))[0],compose(c[5],F2Lsquisher((c[6],c[7]))[0]))))
                                nextappend = nextappend + F2Lsquisher((c[0],c[1]))[1]
                                if c[2] == U:
                                    nextappend.append("U")
                                if c[2] == Ui:
                                    nextappend.append("Ui")
                                if c[2] == U2:
                                    nextappend.append("U2")
                                nextappend = nextappend + F2Lsquisher((c[3],c[4]))[1]
                                if c[5] == U:
                                    nextappend.append("U")
                                if c[5] == Ui:
                                    nextappend.append("Ui")
                                if c[5] == U2:
                                    nextappend.append("U2")
                                nextappend = nextappend + F2Lsquisher((c[6],c[7]))[1]
                                break
                            testing_scramble = working_scramble.copy()
                        else:
                            nextsol = U
                            nextappend = ["U"]
        
        working_scramble = compose(working_scramble,nextsol)
        sol = sol + nextappend
    return sol

def SolveOll(scramble):
    working_scramble = scramble.copy()
    EdgOs = [0,0,0,0]
    num = 0
    sol = []
    for i in [(1,0),(3,1),(5,2),(7,3)]:
        if inverse(scramble)[i[0]] in Up:
            EdgOs[i[1]] = 1
            num = num + 1
    if num == 0:
        sol = ["F", "U", "R", "Ui", "Ri", "Fi", "Ui", "F", "R", "U", "Ri", "Ui", "Fi"]
        working_scramble = compose(working_scramble, convert(sol))
    elif num == 2:
        if EdgOs[1] == 1 and EdgOs[2] == 1:
            sol = ["F", "R", "U", "Ri", "Ui", "Fi"]
            working_scramble = compose(working_scramble, convert(sol))
        elif EdgOs[0] == 1 and EdgOs[3] == 1:
            sol = ["U", "F", "R", "U", "Ri", "Ui", "Fi"]
            working_scramble = compose(working_scramble, convert(sol))
        elif EdgOs[0] == 1 and EdgOs[1] == 1:
            sol = ["F", "U", "R", "Ui", "Ri", "Fi"]
            working_scramble = compose(working_scramble, convert(sol))
        elif EdgOs[0] == 1 and EdgOs[2] == 1:
            sol = ["Ui", "F", "U", "R", "Ui", "Ri", "Fi"]
            working_scramble = compose(working_scramble, convert(sol))
        elif EdgOs[1] == 1 and EdgOs[3] == 1:
            sol = ["U", "F", "U", "R", "Ui", "Ri", "Fi"]
            working_scramble = compose(working_scramble, convert(sol))
        elif EdgOs[2] == 1 and EdgOs[3] == 1:
            sol = ["U2", "F", "U", "R", "Ui", "Ri", "Fi"]
            working_scramble = compose(working_scramble, convert(sol))
    CornOs = [0,0,0,0]
    for corner in [(0,27,20,0),(2,11,18,1),(6,29,36,2),(8,9,38,3)]:
        if inverse(working_scramble)[corner[0]] in Up:
            CornOs[corner[3]] = 2
        elif inverse(working_scramble)[corner[1]] in Up:
            CornOs[corner[3]] = 1
    if CornOs == [0,0,0,0]:
        tempsol = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,1,1,1]:
        tempsol = ["U", "F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,1,0,0]:
        tempsol = ["U", "R", "U2", "R2", "Ui", "R2", "Ui", "R2", "U2", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,0,1,0]:
        tempsol = ["R", "U2", "R2", "Ui", "R2", "Ui", "R2", "U2", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,0,1,1]:
        tempsol = ["Ui", "R", "U2", "R2", "Ui", "R2", "Ui", "R2", "U2", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,1,0,1]:
        tempsol = ["U2", "R", "U2", "R2", "Ui", "R2", "Ui", "R2", "U2", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,1,2,0]:
        tempsol = ["R", "U", "Ri", "U", "R", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,1,1,0]:
        tempsol = ["Ui", "R", "U", "Ri", "U", "R", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,2,1,0]:
        tempsol = ["U2", "R", "U", "Ri", "U", "R", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,1,1,2]:
        tempsol = ["U", "R", "U", "Ri", "U", "R", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,2,0,1]:
        tempsol = ["R", "U2", "Ri", "Ui", "R", "Ui", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,0,0,2]:
        tempsol = ["Ui", "R", "U2", "Ri", "Ui", "R", "Ui", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,0,2,1]:
        tempsol = ["U2", "R", "U2", "Ri", "Ui", "R", "Ui", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,0,0,1]:
        tempsol = ["U", "R", "U2", "Ri", "Ui", "R", "Ui", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,1,0,2]:
        tempsol = ["Ri", "F", "R", "Bi", "Ri", "Fi", "R", "B"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,2,2,0]:
        tempsol = ["Ui", "Ri", "F", "R", "Bi", "Ri", "Fi", "R", "B"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,0,1,2]:
        tempsol = ["U2" "Ri", "F", "R", "Bi", "Ri", "Fi", "R", "B"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,2,2,1]:
        tempsol = ["U" "Ri", "F", "R", "Bi", "Ri", "Fi", "R", "B"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,1,2,2]:
        tempsol = ["Bi", "Ri", "F", "R", "B", "Ri", "Fi", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,0,2,0]:
        tempsol = ["Ui", "Bi", "Ri", "F", "R", "B", "Ri", "Fi", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,2,1,1]:
        tempsol = ["U2", "Bi", "Ri", "F", "R", "B", "Ri", "Fi", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,2,0,2]:
        tempsol = ["U", "Bi", "Ri", "F", "R", "B", "Ri", "Fi", "R"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,2,0,0]:
        tempsol = ["R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [1,2,1,2]:
        tempsol = ["Ui","R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [0,0,2,2]:
        tempsol = ["U2", "R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    elif CornOs == [2,1,2,1]:
        tempsol = ["U", "R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
        working_scramble = compose(working_scramble, convert(tempsol))
        sol = sol + tempsol
    return sol


def SolvePLL(scramble: list):
    working_scramble = scramble.copy()
    Eperm = [0,0,0,0]
    Cperm = []
    sol = []
    Estickers = [10,19,28,37]
    Cstickers = [0,2,6,8]
    while numsolved(working_scramble,Estickers)<4 and len(sol) < 100:
        i = 0
        for edge in Estickers:
            Eperm[i] = working_scramble[edge]
            i = i+1
        if Eperm == [37,28,19,10]:
            tempsol = ["R2", "L2", "D", "R2", "L2", "U", "Ri", "Li", "F2", "R2", "L2", "B2", "Ri", "Li", "U2"]
            working_scramble = compose(working_scramble,convert(tempsol))
            sol = sol + tempsol
        elif Eperm == [28,19,37,10]:
            tempsol = ["R2", "U", "R", "U", "Ri", "Ui", "Ri", "Ui", "Ri", "U", "Ri"]
            working_scramble = compose(working_scramble,convert(tempsol))
            sol = sol + tempsol
        elif Eperm == [10,28,37,19]:
            tempsol = ["Ui", "R2", "U", "R", "U", "Ri", "Ui", "Ri", "Ui", "Ri", "U", "Ri", "U"]
            working_scramble = compose(working_scramble,convert(tempsol))
            sol = sol + tempsol
        elif Eperm == [37,19,10,28]:
            tempsol = ["R", "Ui", "R", "U", "R", "U", "R", "Ui", "Ri", "Ui", "R2"]
            working_scramble = compose(working_scramble,convert(tempsol))
            sol = sol + tempsol
        elif Eperm == [37,10,28,19]:
            tempsol = ["U", "R", "Ui", "R", "U", "R", "U", "R", "Ui", "Ri", "Ui", "R2", "Ui"]
            working_scramble = compose(working_scramble,convert(tempsol))
            sol = sol + tempsol
        else:
            tempsol = ["U"]
            working_scramble = compose(working_scramble,convert(tempsol))
            sol = sol + tempsol
    
    for corner in Cstickers:
        Cperm.append(working_scramble[corner])
    if Cperm == [8,0,6,2]:
        tempsol = ["Ri", "F", "Ri", "B2", "R", "Fi", "Ri", "B2", "R2"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [6,0,2,8]:
        tempsol = ["U", "Ri", "F", "Ri", "B2", "R", "Fi", "Ri", "B2", "R2", "Ui"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [6,2,8,0]:
        tempsol = ["U2", "Ri", "F", "Ri", "B2", "R", "Fi", "Ri", "B2", "R2", "U2"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [0,6,8,2]:
        tempsol = ["Ui", "Ri", "F", "Ri", "B2", "R", "Fi", "Ri", "B2", "R2", "U"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [2,8,6,0]:
        tempsol = ["R2", "B2", "R", "F", "Ri", "B2", "R", "Fi", "R"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [2,6,0,8]:
        tempsol = ["U", "R2", "B2", "R", "F", "Ri", "B2", "R", "Fi", "R", "Ui"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [8,2,0,6]:
        tempsol = ["U2", "R2", "B2", "R", "F", "Ri", "B2", "R", "Fi", "R", "U2"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [0,8,2,6]:
        tempsol = ["Ui", "R2", "B2", "R", "F", "Ri", "B2", "R", "Fi", "R", "U"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [6,8,0,2]:
        tempsol = ["R", "Bi", "Ri", "F", "R", "B", "Ri", "Fi", "R", "B", "Ri", "F", "R", "Bi", "Ri", "Fi"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [2,0,8,6]:
        tempsol = ["U", "R", "Bi", "Ri", "F", "R", "B", "Ri", "Fi", "R", "B", "Ri", "F", "R", "Bi", "Ri", "Fi", "Ui"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    elif Cperm == [8,6,2,0]:
        tempsol = ["R2", "L2", "D", "R2", "L2", "U2", "R2", "L2", "D", "R2", "L2", "U2"]
        working_scramble = compose(working_scramble,convert(tempsol))
        sol = sol + tempsol
    return sol
    
    


    

    
            






        
        
def CFOP2LookSolver(moves):
    scramble = Unstringify(moves)

    crossSol = SolveCross(scramble)
    scramble = compose(scramble,convert(crossSol))

    F2LSol = SolveF2L(scramble)
    scramble = compose(scramble,convert(F2LSol))
    
    OLLSol = SolveOll(scramble)
    scramble = compose(scramble,convert(OLLSol))

    PLLSol = SolvePLL(scramble)
    scramble = compose(scramble,convert(PLLSol))

    Sol = crossSol + F2LSol + OLLSol + PLLSol
    return Sol


print(CFOP2LookSolver("R L F B D Fi Bi L2 R2 D2 U2 R Ui Ri U2 B F2 Li"))
