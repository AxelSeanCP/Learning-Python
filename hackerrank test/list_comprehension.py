"""
 You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
 Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k) is not equal n.
 example:
 x = 1
 y = 1
 z = 1
 n = 2
 output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

x = 1
y = 2
z = 3
n = 3

output = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print(output)