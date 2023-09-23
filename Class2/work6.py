def Square_root_3(c):
    g=c/4
    i=0
    b=0
    while(abs(g * g - c)>0.00000000001):
        g=(g+c/g)/2
        i+=1
        b=i
    print("%.8f %d"%(g,b))
c=int(input())
Square_root_3(c)
