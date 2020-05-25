# Challenge Summary
matrix array : insert integer to middle of array

## Challenge Description
Ask the candidate to write a function to add up the sum of each row in a matrix of arbitrary size, and return an array with the appropriate values.
Avoid utilizing any of the built-in methods available to your language.
Don’t let the candidate get scared by the term “matrix”… It’s just an array of arrays.
The matrix will always be full of integers.
Negative values are possible.
All nulls will be counted as zeros.

## Approach & Efficiency
loop through first array of arrays, for each index in the range of that indexed array, increment counter. append the counter value to the output array to record the total value of that small array. move to the next small array in the large array. return the output array of the values for each array. 

## Solution
![matrix array whiteboard image](/assets/matrix_array.png)