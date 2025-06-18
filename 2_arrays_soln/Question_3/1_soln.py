# 1. Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

maxNo = int(input("Enter the last number: "))
l = [i for i in range(1,maxNo+1) if i%2 != 0]
print(l)
