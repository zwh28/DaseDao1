def Square_root_1(n):
    g=0
    for j in range(0,n+1):
        if(j * j > n and g == 0):
            g = j - 1
    while(abs(g * g - n) > 0.0001):
        g += 0.00001
    print("%.5f" %g)

n=int(input())
Square_root_1(n)

