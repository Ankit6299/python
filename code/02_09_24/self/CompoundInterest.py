P = int(input("Enter p:"))
R = int(input("Enter r:"))
N = int(input("Enter n:"))
T = int(input("Enter t:"))

def compound_interest(p,r,n,t):
    print('The principal is', p)
    print('The rate is', r)
    print('The time period is', n)
    print('The times interest is compounded per year is ', t)

    ci = p*(1+(r/n))**n*t

    return ci

print("Amount is ",compound_interest(P,R,N,T))
