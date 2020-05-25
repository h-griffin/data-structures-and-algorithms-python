# Challenge Summary
insert shift array : insert integer to middle of array

## Challenge Description
Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
split the array in half by length by using len() if it is even continue if it is odd add 0.5 to give middle place. rebuilt array one by one in for loop, if the index is less than the previously decided middle value, append to the empty array. if the value is equal to the middle value append the middle value then the new integer. if the index is greater than the middle value, append.

## Solution
![array shift whiteboard image](/assets/array_shift.png)
