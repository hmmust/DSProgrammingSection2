def square(n):
    return n*n  #n**2 or pow(n,2)
"""def squares(n):
    yield n*n  #n**2 or pow(n,2)
    yield n**3 
    yield n**4  """
"""def squares(n):
    for i in range(1,n+1):
        yield i**2  #n**2 or pow(n,2)
"""
squares= (i**2 for i in range(1,11))
        
for i  in squares:
    print(i)

#print( [*range(1,11)])
"""for i in range(1,11,2):
    print(i)
for i in range(10,0,-1):
    print(i)"""