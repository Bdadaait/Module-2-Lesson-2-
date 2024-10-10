# Task 1: Leap Year Checker

year= int(input("Enter a year: "))

if (year % 4 == 0  and year % 100 != 0):
   print ( f"{year}  is a yeap year")
    
elif (year % 400 == 0): 
   print ( f"{year}  is a yeap year")
    
else :
   print ( f"{year}  is not a yeap year")  