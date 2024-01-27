Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.

Submissions: 32
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
​
10
​
11
if __name__ == '__main__':
12
    n = int(input().strip())


OUTPUT:



#!/bin/python3

import math
import os
import random
import re
import sys
def sum_of_digits(num):
    return sum(map(int, str(num)))

def best_divisor(n):
    best_div = 1
    max_digit_sum = 1

    for divisor in range(2, n + 1):
        if n % divisor == 0:
            digit_sum = sum_of_digits(divisor)
            if digit_sum > max_digit_sum or (digit_sum == max_digit_sum and divisor < best_div):
                best_div, max_digit_sum = divisor, digit_sum

    return best_div



if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result)
