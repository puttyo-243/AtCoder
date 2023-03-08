import math

input_list = list(map(int,input().split()))
A = input_list[0]
B = input_list[1]
C = input_list[2]
ab_gcd = math.gcd(A,B)
gcd = math.gcd(ab_gcd,C)
print(((A//gcd) - 1) + ((B//gcd) - 1) + ((C//gcd) - 1))