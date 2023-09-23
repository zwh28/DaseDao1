def cube_root_binary(n):
    l = 0
    r = max(1, n)  # 取1和n中的较大值作为右边界

    while abs(r - l) > 1e-8:
        mid = (l + r) / 2
        if mid ** 3 >= n:
            r = mid
        else:
            l = mid

    return l


n = float(input("请输入一个大于等于1的实数: "))
result = cube_root_binary(n)
print("{:.6f}".format(result))
