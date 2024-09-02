#SimpleInterest.py

P = int(input("Enter p:"))
R = int(input("Enter r:"))
T = int(input("Enter t:"))

def simple_interest(p,r,t):
    print('The principal is', p)
    print('The rate is', r)
    print('The time period is', t)

    si = (p*r*t)/100

    return si

print("si is ",simple_interest(P,R,T))
