# a program which asks the user to enter an integer 'n' which 
# would be the total numbers of hours the user worked in a week
# and calculates and prints the total amount of money the user 
# made during that week. If the user enters any number less than
# 0 or greater than 168 (n < 0 or n > 168) then your program should
# print INVALID


# Type your code here
n = input("please enter your worktime (hour): ")
n = int(n)
if n < 0 or n > 168:
    print("INVALID")
elif n >= 0 and n <= 40:
    MONEY = n * 8
    print("YOU MADE",MONEY, "DOLLARS THIS WEEK")
elif n >= 41 and n <= 50:
    DIFF = n - 40
    MONEY = (40 * 8) + (DIFF * 9)
    print("YOU MADE",MONEY, "DOLLARS THIS WEEK")
else:
    DIFF = n - 50
    MONEY = (40 * 8) + (10 * 9) + (DIFF * 10)
    print("YOU MADE",MONEY, "DOLLARS THIS WEEK")
