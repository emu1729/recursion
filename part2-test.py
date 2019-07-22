import part2
import csv

mylist = []
with open('list_of_numbers.csv', 'r') as csvfile:
    for row in csv.reader(csvfile, delimiter=';'):
        mylist.append(int(row[0]))

print("Exercise 1")

if part2.sortFirst(mylist) == range(1, 10001):
	print("Passed")
else:
	print("Failed")

print("Exercise 2")

if part2.sortSecond(mylist) == range(1, 10001):
	print("Passed")
else:
	print("Failed")