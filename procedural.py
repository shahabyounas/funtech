print('Program Starts')

count = 0
total = 0

while count < 5:
#While the value of count is less than five


       number = int(input(f"Type in a number {count + 1}\t"))
       #Input a number

       total = total + number
       #Add the number to the total

       count = count + 1
       #Add one to the value of count
    

print("The total is ", total)
    
#Print out the total

print('Program Ended')