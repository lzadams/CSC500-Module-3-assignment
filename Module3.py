#CSC500 Module 3 assignment
#Part 1:Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts with
# an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.


charge_for_the_food = float(input('Enter the charge for the food: $'))
tip = 0.18 * charge_for_the_food
sales_tax = 0.07 * charge_for_the_food
total_price = charge_for_the_food + tip + sales_tax
print('Charge for the food is:','${}'.format(charge_for_the_food))
print ('Tip is:','${}'.format(tip))
print('Total price is:','${}'.format(total_price))

#Part 2:
#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

#Ask the user for the time now (in hours)
current_time = float (input ('What time is it now (in hours)?'))
#Ask for the number of hours to wait for the alarm
waiting_hours = float (input ('How many hours are you waiting for the alarm?'))
#Calculate the alarm time within a 24-hour clock
total_time = current_time + waiting_hours
alarm_time = total_time % 24
hour = int (alarm_time)
min = int ((alarm_time - hour) * 60)
second = int(((alarm_time - hour) * 3600) % 60)
#print out the time when the alarm goes off
print(f'It will be {hour:02}:{min:02}:{second:02} when the alarm goes off')
