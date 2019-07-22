import part1

print("Part 1 Tests")

print("Exercise 1")

s = "Hello" + "\n" + "Hello" + "\n" + "Hello" + "\n" 

if part1.repeatPrint("Hello", 3) == s:
	print("Passed")
else:
	print("Failed")

print("Exercise 2")

if part1.repeatPrintRecursive("Hello", 3) == s:
	print("Passed")
else:
	print("Failed")

print("Exercise 3")

if part1.fibonacci(5) == 5 and part1.fibonacci(14)==377:
	print("Passed")
else:
	print("Failed")

print("Exercise 4")

if part1.fibonacciRecursive(5) == 5 and part1.fibonacciRecursive(14)==377:
	print("Passed")
else:
	print("Failed")