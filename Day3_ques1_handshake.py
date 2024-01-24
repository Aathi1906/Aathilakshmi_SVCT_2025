At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example

There are  attendees, ,  and .  shakes hands with  and , and  shakes hands with . Now they have all shaken hands after  handshakes.

Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees
Returns

int: the number of handshakes
Input Format
The first line contains the number of test cases .
Each of the following  lines contains an integer, .

Constraints



Sample Input

2
1
2
Sample Output

0
1
Explanation

Case 1 : The lonely board member shakes no hands, hence 0.
Case 2 : There are 2 board members, so 1 handshake takes place.

Contest ends in a day
Submissions: 5
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
# Complete the 'handshake' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts INTEGER n as parameter.
14
#
15
​
16
def handshake(n):
17
    # Write your code here
18
​
19
if __name__ == '__main__':
20
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
21
​
22
    t = int(input().strip())
23
​
24
    for t_itr in range(t):
25
        n = int(input().strip())
26
​
27
        result = handshake(n)
28
​
29
        fptr.write(str(result) + '\n')
30
​
31
    fptr.close()
32
​


OUTPUT:


def handshake(n):
    # Write your code here
    return n * (n - 1) // 2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
