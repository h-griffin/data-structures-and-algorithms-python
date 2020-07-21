# Challenge Summary
insert shift array : insert integer to middle of array

## Challenge Description
Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
split the array in half by length by using len() if it is even continue if it is odd add 0.5 to give middle place. rebuilt array one by one in for loop, if the index is less than the previously decided middle value, append to the empty array. if the value is equal to the middle value append the middle value then the new integer. if the index is greater than the middle value, append.

## Solution
![array shift whiteboard image](/assets/array_shift.png)


### Code Challenge
Insert and shift an array in middle at index

Specifications
Read all of these instructions carefully. Name things exactly as described.
Do all your work in a public repository called data-structures-and-algorithms.
Create a new branch in your repo called array-shift.
Your top-level readme should contain a “Table of Contents” navigation to all of your challenges and implementations so far. (Don’t forget to update it!)
This assignment should be completed within the challenges subdirectory of the repository.
On your branch, create…
C#: a new .NET Core console project named ArrayShift. Within your Program.cs create a new static method outside of Main() following the naming conventions below. Call your newly created method in Main() once complete.
JavaScript: a folder named arrayShift which contains a file called array-shift.js
Python: a folder named array_shift which contains a file called array_shift.py
Java: a file called ArrayShift.java
Include any language-specific configuration files required for this challenge to become an individual component, module, library, etc.
NOTE: You can find an example of this configuration for your course in your class lecture repository.
Feature Tasks
Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
Example
``` Input	Output
[2,4,6,8], 5	[2,4,5,6,8]
[4,8,15,23,42], 16	[4,8,15,16,23,42]
```
Stretch Goal
Once you’ve achieved a working solution, write a second function that removes an element from the middle index and shifts other elements in the array to fill the new gap.

Requirements
Ensure your complete solution follows the standard requirements.

Write unit tests
Follow the template for a well-formatted README
Submit the assignment following these instructions
