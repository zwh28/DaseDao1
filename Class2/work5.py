def Square_root_3(c):
    g=c/2
    while(abs(g * g - c)>0.00000000001):
        g=(g+c/g)/2
    print("%.8f"%g)
c=int(input())
Square_root_3(c)
