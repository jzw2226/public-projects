#initialize by creating variables and getting values from user 

ones = 0
fives = 0
tens = 0
twenties = 0
fifties = 0
hundreds = 0
temp_num = 0
total_amount = int(input("Please enter the amount of money you wish to withdraw: "))

#get number of hundred dollar bills

temp_num = total_amount
total_amount %= 100
hundreds = (temp_num - total_amount)/100

#get number of fifty dollar bills

temp_num = total_amount
total_amount %= 50
fifties = (temp_num - total_amount)/50

#get number of twenty dollar bills

temp_num = total_amount
total_amount %= 20
twenties = (temp_num - total_amount)/20

#get number of ten dollar bills

temp_num = total_amount
total_amount %= 10
tens = (temp_num - total_amount)/10

#get number of five dollar bills

temp_num = total_amount
total_amount %= 5
fives = (temp_num - total_amount)/5

#get number of one dollar bills

temp_num = total_amount
total_amount %= 1
ones = (temp_num - total_amount)/1

#print final results

print(f"You received {hundreds:.0f} hundred(s)\nYou received {fifties:.0f} fifty(s)\nYou received {twenties:.0f} twenty(s)\nYou received {tens:.0f} ten(s)\nYou received {fives:.0f} five(s)\nYou received {ones:.0f} one(s)")


