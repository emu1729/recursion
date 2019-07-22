## Y2 2019 Summer: Challenge Recursion Lab

Welcome to your introduction on algorithms and asymptotics!

### Part 1. Recursion

The stubs for these functions can be found in `part1.py`. You can test your functions by running `part1-test.py`.

What is recursion? It's basically a function that calls itself!

1. Write a function called repeatPrint that prints out a section of text some numberOfTimes. Use a for loop.

2. Now try writing a recursive version of that function does the same thing. Remember that a recursive function must have a base case and a recursive case!

**Hint: What is the smallest number of times something can be repeated? This might be your base case**

3. Do you know the Fibonacci sequence? 0, 1, 1, 2, 3, 5, ... etc. Let's write a Fibonacci sequence function using for loops.

4. Alright great job! Now try using recursion. What are your base cases? Is this shorter or longer than your exercise 3?

5. Get ya checkoff! 

### Part 2. Sorting

The stubs for these functions can be found in `part2.py`. You can test your functions by running `part2-test.py`.

Let's start this journey by considering a VERY important function: sorting.

1. Alright, now we have a VERYYY long list of numbers. We want to sort them in ascending order. The first way we can do this is by iterating through the list over and over again and finding the smallest remaining value. Let's try this method first.

2. You might think this is kind of inefficient. And you'd be right! This kind of method might take a super LONG time if we have a very LONG list. How can we write a recursive method to do this?

**Hint: What if we break it into halves and recurse on each half? How do we merge the two halves together? What is our base case?**

### Part 3. Wanna learn more?

1. Read this site and do the practice:
https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation

2. Let's analyze the algorithms we wrote in part 2. What is the asymptotic runtime of each?

