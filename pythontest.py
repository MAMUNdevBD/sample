# Problem 1

#print("Assalamualikum")

#Problem 2

#a, b = list(map(int,input().split(" ")))
#S = a+b
#print(S)

#problem 3

#a, b = list(map(int, input().split(" ")))

#if b != 0:
#    d = a/b
#    r = a%b
#    if(r == 0):
#        print(f"{a} is divisible by {b}")
#    else:
#        print(f"{a} is not divisible by {b}, and the remainder is {r}.")


#problem 4

n = int(input())

i = 0
j = 0

while i < n:
   j = j+(n-i)
   i += 1

print(j)

#problem 5

n = int(input())

i = 0
j = 0

while i < n:
    l = n-i
    k = n - l
    if((k%3 == 0 or k%5 == 0) and k != 0):
       j = j+k
       print(k," ", end="")
    i += 1

print("=",j)
