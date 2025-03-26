# i. Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)
# ii. Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2)
num =int(input("enter a number"))
sum = (num*(num+1))//2
print("sum of ",num,"natural number is:",sum)

# iii. Print all even numbers between 1 and 50 using a while
# loop.
num = 2
while num <=50:
    print(num)
    num+=2
# iv. Write a program to display the multiplication table of a given
# number. First 20
# tables
num = int(input("enter the number upto which tables should be displayed:"))
for i in range(1,num + 1):
    for j in range(1,21):
        print(i,'x',j,'=',i*j)

# v. Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits.
# vi. Write a program to count the number of digits in a given
# number using a while loop.


# reverse an interger
rev=0
sum = 0
count = 0
num = int(input("enter the integer"))
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    print (rem)
    num = num // 10
    sum += rem
    count+=1

print(rev)
print(count)
print(sum)

# vii. Write a program that keeps asking the user to enter numbers
# until they enter a negative number. Use a while loop.

num = int(input("enter a number"))
while num >= 0:
    print("enter a negative number to stop")
    break
print("negative number entered")


