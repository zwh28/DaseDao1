def Cube_root(c):
    g=c/2
    while(abs(g*g*g-c)>0.00000000001):
        g=(2*g+c/g**2)/3
    print("%.6f"%g)
n=int(input())
Cube_root(n)
