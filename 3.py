Z={}

def union(A,B):
    for x in A and B:
        Z[x] = max(A[x],B[x])
    return Z

def intersection(A,B):
    for x in A and B:
        Z[x] = min(A[x],B[x])
    return Z

def complement(X):
    for x in X:
        Z[x] = round(1-X[x],2)
    return Z

def get_membership_value(key):
    while True:
        value=float(input("Enter the membership values(btw 0 and 1) for "+key))
        if 0<= value <= 1:
            return value
        else:
            print("enter valid number")

A={}
B={}

no_items = int(input("Enter the numbers:"))

for _ in range(no_items):
    key = input("Enter the crispy set elements: ")
    value = get_membership_value(key)
    A[key] = value
    value = get_membership_value(key)
    B[key] = value


print(f"{A=} UNION {B=} is {union(A,B)}")
print(f"{A=} Intersection {B=} is {intersection(A,B)}")
print(f" complement of {A=} is {complement(A)}")
print(f" complement of {B=} is {complement(B)}")




    
