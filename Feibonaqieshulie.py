def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = input('请输入斐波那契数列的长度：')
for i in range(1,int(n)+1):
    print('f(%s)=%s'%(i,fib(i)))               #斐波那契数列
