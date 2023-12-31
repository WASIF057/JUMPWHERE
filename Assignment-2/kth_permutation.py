#With the range of numbers from 1 to n inclusive, we can make n! permutations. By labeling them in order starting from 1, you are asked to return the kth permutation

def  kth_permutation(n, k):
    permutation = []
    unused = list(range(1, n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    k -= 1
    while n> 0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        unused.pop(i)
        n -= 1 
        k %= part_length
    return ''.join(map(str, permutation))
    
n = 3
k = 3
print(kth_permutation(n, k))
