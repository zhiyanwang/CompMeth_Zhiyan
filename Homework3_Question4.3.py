x0 = float(input("Please enter the number for derivative calculation: "))


def f(x):
    f = x*(x-1)
    return f

def df(x):
    delta = float(input("Please enter the accuracy for derivative calculation: "))
    df = (f(x+delta)-f(x-delta))/delta
    return df

y0 = df(x0)

print("The derivative is: ", y0)

print("The difference is: ", (2-y0))

# Analytically the derivative at x=1 is 2
# The result for delta = 10^-2 is 2.0000000000000018, with difference -1.8e-15
# The reason is that the computer stores a number in binary,
# so it won’t necessarily store the same value as expected.
# The smallest accuracy is about 10^-16, thus giving this difference.


# The result for delta = 10^-4 is 1.9999999999997797, with difference 2.203e-13
# The result for delta = 10^-6 is 1.999999999946489, with difference 5.3511e-11
# The result for delta = 10^-8 is 1.9999999989472879, with difference 1.0527121e-09
# The result for delta = 10^-10 is 2.000000165480742, with difference -1.65480742e-07
# The result for delta = 10^-12 is 2.0000667788622195, with difference -6.67788622195e-05
# The result for delta = 10^-14 is 1.9984014443252818, with difference 1.5985556747182e-03


# The accuracy of the calculation gets worse as delta gets smaller