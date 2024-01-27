Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

Example



The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

Function Description

Complete the solve function in the editor below.

solve has the following parameters:

int n: the number of candy jars
int operations[m][3]: a 2-dimensional array of operations
Returns

int: the floor of the average number of canidies in all jars
Input Format

The first line contains two integers,  and , separated by a single space.
 lines follow. Each of them contains three integers, , , and , separated by spaces.

Constraints





Sample Input

STDIN       Function
-----       --------
5 3         n = 5, operations[] size = 3
1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
2 5 100
3 4 100
Sample Output

160
Explanation

Initially each of the jars contains 0 candies

0 0 0 0 0  
First operation:

100 100 0 0 0  
Second operation:

100 200 100 100 100  
Third operation:

100 200 200 200 100  
Total = 800, Average = 800/5 = 160

Submissions: 27
Max Score: 10
Difficulty: Easy
Rate This Challenge:

    
More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
#
10
# Complete the 'solve' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts following parameters:
14
#  1. INTEGER n
15
#  2. 2D_INTEGER_ARRAY operations
16
#
17
​
18
def solve(n, operations):
19
    # Write your code here
20
​
21
if __name__ == '__main__':
22
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
23
​
24
    first_multiple_input = input().rstrip().split()
25
​
26
    n = int(first_multiple_input[0])
27
​
28
    m = int(first_multiple_input[1])
29
​
30
    operations = []
31
​
32
    for _ in range(m):
33
        operations.append(list(map(int, input().rstrip().split())))
34
​
35
    result = solve(n, operations)
36
​
37
    fptr.write(str(result) + '\n')
38
​
39
    fptr.close()
40
​


OUTPUT:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

def solve(n, operations):
    total_candies = 0
    for operation in operations:
        start_index, end_index, candies = operation
        total_candies += (end_index - start_index + 1) * candies

    average = total_candies // n
    return average

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()



