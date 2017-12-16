from math import sin,cos,pi,e
import matplotlib.pyplot as plt

# Task 1: (Deltoid Curve) Calculate x1 and y1, then plot y1 as a function of x1.

points1 = 500

space1 = 2*pi/points1

x1 = []

y1 = []

n1 = 0

for n1 in range(points1):
    theta1 = n1 * space1
    x1 += [2*cos(theta1)+cos(2*theta1)]
    y1 += [2*sin(theta1)-sin(2*theta1)]

plt.plot(x1,y1,"blue")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("First Task: Deltoid Curve")
plt.show()
plt.savefig("Homework2_Question3.2_FirstTask_DeltoidCurve.png")

# Task 2: (Galilean spiral) Calculate x2 and y2, then plot y2 as a function of x2.

points2 = 2500

space2 = 10*pi/points2

x2 = []

y2 = []

n2 = 0

for n2 in range(points2):
    theta2 = n2 * space2
    r2 = theta2**2
    x2 += [r2*cos(theta2)]
    y2 += [r2*sin(theta2)]

plt.plot(x2,y2,"green")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Second Task: Galilean spiral")
plt.show()
plt.savefig("Homework2_Question3.2_SecondTask_GalileanSpiral.png")

# Task 3: (Fey’s function) Calculate x3 and y3, then plot y3 as a function of x3.

points3 = 6000

space3 = 24*pi/points3

x3 = []

y3 = []

n3 = 0

for n3 in range(points3):
    theta3 = n3 * space3
    r3 = e**cos(theta3)-2*cos(4*theta3)-(sin(theta3/12)**5)
    x3 += [r3*cos(theta3)]
    y3 += [r3*sin(theta3)]


plt.plot(x3,y3,"purple")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Third Task: Fey’s function")
plt.show()
plt.savefig("Homework2_Question3.2_ThirdTask_Fey’sFunction.png")