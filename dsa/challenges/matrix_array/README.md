# Challenge Summary
matrix array : insert integer to middle of array

## Challenge Description
- Ask the candidate to write a function to add up the sum of each row in a matrix of arbitrary size, and return an array with the appropriate values.
- Avoid utilizing any of the built-in methods available to your language.
- Don’t let the candidate get scared by the term “matrix”… It’s just an array of arrays.
- The matrix will always be full of integers.
- Negative values are possible.
- All nulls will be counted as zeros.

## Approach & Efficiency
loop through first array of arrays, for each index in the range of that indexed array, increment counter. append the counter value to the output array to record the total value of that small array. move to the next small array in the large array. return the output array of the values for each array.

## Solution
![matrix array whiteboard image](/assets/matrix_array.png)

### Structure
Familiarize yourself with the grading rubric, so you know how to score the interview.

Look for effective problem solving, efficient use of time, and effective communication with the whiteboard space available.

Every solution might look a little different, but the candidate should be able to at least convince you that their code works to solve the problem.

Assign points for each item on the Rubric, according to how well the candidate executed on that skill.

Add up all the points at the end, and record the total at the bottom of the page.

Example
```Input	Output
[ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]	[6, 15, 18]
[ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ]	[6, 5, 20]
```
The candidate should draw the input and output as a square of integers.

Documentation
Record detailed notes on the rubric, to share with the candidate when the interview is complete.
