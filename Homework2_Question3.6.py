# 3.6 Deterministic chaos and the Feigenbaum plot

import matplotlib.pyplot as plt
import numpy as np


################### Method 1 ###################

x_array=[]

r_array=[]

r=1

x_range=1000

r_space=0.01

r_range = 300

for n in range(r_range):
    x = 1 / 2
    r = 1+n*r_space
    for m in range(x_range):
         x = r*x*(1-x)
    x_array += [x]
    r_array += [r]


plt.plot(r_array,x_array,"k.")
plt.xlabel("r-axis")
plt.ylabel("x-axis")
plt.title("Logistic Map")
plt.show()
plt.savefig("Homework2_Question3.6_LogisticMap.png")

# Answer to questions:

# 1. For a given value of r, a fixed point would gradually be approached on from the initial x value.
# And with r increasing, the fixed point for each r also changes.

# 2. For a given value of r, a limit cycle shows that the value of x oscillate periodically within a certain range.
# And with r increasing, the range of limit cycle for each r also changes.

# 3. For a given value of r, chaos result appears random but is limited within a certain range.
# And with r increasing, the range of chaos for each r also changes.

# 4. At r = 3.57, the system move from orderly behavior to chaotic behavior.

################### Method 2 (Using array) from Comment ###################

r2_list=[]

r=1.0

r_space=0.01

r_range = 300

for n in range(r_range):
    r2_list += [r]
    r = 1.0+n*r_space

x2_list=[]
for m in range(len(r2_list)):
    x2_list += [0.5]

r2_array=np.array(r2_list)
x2_array=np.array(x2_list)

for l in range(1000):
    x2_array = r2_array*x2_array*(1-x2_array)

plt.plot(r2_array,x2_array,"k.")
plt.xlabel("r-axis")
plt.ylabel("x-axis")
plt.title("Logistic Map")
plt.show()
#plt.savefig("Homework2_Question3.6_Logistic Map_Method2.png")