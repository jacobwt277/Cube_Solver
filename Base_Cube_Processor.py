def compose(x: list,y: list): #So we can compose permutations. Done left to right, not in function notation order, so that it matches cuber notation.
    i = 0
    w = x.copy()
    for c in x:
        w[i] = y[c]
        i = i+1

    return w

def inverse(x: list): #So we can invert permutations.
    z = x.copy()
    i = 0
    for c in x:
        z[c] = i
        i = i+1
    
    return z


R = [0,1,24,3,4,21,6,7,18,11,14,17,10,13,16,9,12,15,53,19,20,50,22,23,47,25,26,27,28,29,30,31,32,33,34,35,36,37,2,39,40,5,42,43,8,45,46,38,48,49,41,51,52,44]
U = [2,5,8,1,4,7,0,3,6,36,37,38,12,13,14,15,16,17,9,10,11,21,22,23,24,25,26,18,19,20,30,31,32,33,34,35,27,28,29,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]
L = [36,1,2,39,4,5,42,7,8,9,10,11,12,13,14,15,16,17,18,19,6,21,22,3,24,25,0,29,32,35,28,31,34,27,30,33,45,37,38,48,40,41,51,43,44,26,46,47,23,49,50,20,52,53]
D = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,25,26,18,19,20,21,22,23,33,34,35,27,28,29,30,31,32,42,43,44,36,37,38,39,40,41,15,16,17,47,50,53,46,49,52,45,48,51]
F = [0,1,2,3,4,5,9,12,15,47,10,11,46,13,14,45,16,17,18,19,20,21,22,23,24,25,26,27,28,8,30,31,7,33,34,6,38,41,44,37,40,43,36,39,42,29,32,35,48,49,50,51,52,53]
B = [33,30,27,3,4,5,6,7,8,9,10,0,12,13,1,15,16,2,20,23,26,19,22,25,18,21,24,51,28,29,52,31,32,53,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,17,14,11]
I = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]

Ri = inverse(R)
Li = inverse(L)
Ui = inverse(U)
Di = inverse(D)
Fi = inverse(F)
Bi = inverse(B)

R2 = compose(R,R)
L2 = compose(L,L)
U2 = compose(U,U)
D2 = compose(D,D)
F2 = compose(F,F)
B2 = compose(B,B)

Moves = [R,U,L,D,F,B,Ri,Ui,Li,Di,Fi,Bi,R2,U2,L2,D2,F2,B2]
Up = {0,1,2,3,4,5,6,7,8}
Right = {9,10,11,12,13,14,15,16,17}
Back = {18,19,20,21,22,23,24,25,26}
Left = {27,28,29,30,31,32,33,34,35}
Front = {36,37,38,39,40,41,42,43,44}
Down = {45,46,47,48,49,50,51,52,53}

def convert(y: list): #Converts a list of moves as strings into a permutation.
    z= I.copy()
    for c in y:
        if c == "R":
            z = compose(z,R)
        elif c == "U":
            z = compose(z,U)
        elif c == "L":
            z = compose(z,L)
        elif c == "D":
            z = compose(z,D)
        elif c == "F":
            z = compose(z,F)
        elif c == "B":
            z = compose(z,B)
        elif c == "Ri":
            z = compose(z,Ri)
        elif c == "Ui":
            z = compose(z,Ui)
        elif c == "Li":
            z = compose(z,Li)
        elif c == "Di":
            z = compose(z,Di)
        elif c == "Fi":
            z = compose(z,Fi)
        elif c == "Bi":
            z = compose(z,Bi)
        elif c == "R2":
            z = compose(z,R2)
        elif c == "U2":
            z = compose(z,U2)
        elif c == "L2":
            z = compose(z,L2)
        elif c == "D2":
            z = compose(z,D2)
        elif c == "F2":
            z = compose(z,F2)
        elif c == "B2":
            z = compose(z,B2)
        else:
            return z
    return z

def Unstringify(stuff):
    return convert(stuff.split())

def numsolved(scramble: list, entries: list):#Checks how many stickers are solved
    num = 0
    for c in entries:
        if scramble[c] == c:
            num = num+1
    return num
