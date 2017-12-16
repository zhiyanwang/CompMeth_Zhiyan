x = int(input("Please enter the number for factotial calculation: "))

# Using integer

def factorial_int(n):
    f = 1.0
    for k in range(1,n+1):
        f *= k
    return f
print("Factorial calculated using integer variable: ", factorial_int(x))

# Using float

f = 1.0
c = 0
m=x
for k in range(1,m+1):
    f *= k
    while f > 10:
        f = f/10
        c += 1
print("Factorial calculated using float-point variable: ", f, "x 10 ^",c)

# Since 200! is bigger than 10^308,
# trying to get it directly with integer will result in overflow error and infinite number.