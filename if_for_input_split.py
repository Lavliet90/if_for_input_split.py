#Write a program that reads a list of numbers list from the first line and a number x from the second line, which prints out all the positions where the number x occurs
#in the given list list.

#Positions are numbered from zero, if the number x is not found in the list, output the string "None" (without quotes, with a capital letter).

#Positions should be displayed on one line, in ascending order of absolute value.


k=0
u=0
a=[int(i) for i in input().split()]
b=int(input())
for z in a:
    k+=1
    if z==b:
        u+=1
        print(k)
if u==0:
    print("None")
