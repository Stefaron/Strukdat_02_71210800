import timeit

def fibo_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
    
def fibo_rec(n):
        if n <= 1:
            return n
        else:
            return(fibo_rec(n-1)+fibo_rec(n-2))
   

for i in range(100+1):
    mulai = timeit.default_timer()
    print('Iterasi ke-{} : {} || {}'.format(i,fibo_iter(i),timeit.default_timer()-mulai))
print('-'*80)

for i in range(100+1):
    mulai = timeit.default_timer()
    print('Iterasi ke-{} : {} || {}'.format(i,fibo_rec(i),timeit.default_timer()-mulai))
print('-'*80)