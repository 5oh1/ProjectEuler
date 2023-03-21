#find all prime factors of 600851475143
val = 600851475143.0
limit = val**(1/2)
factors=[]
primefactors=[]

for i in range(1,int(limit),2):
    if val % i == 0:
        factors.append(int(i))
        factors.append(int(val/i))

for factor in factors[2:]:
    limit = factor**(1/2)
    for i in range(3,int(limit),2):
        if factor % i == 0:
            break
    else:
        primefactors.append(factor)


print("the largest prime factor is",sorted(primefactors)[-1])
