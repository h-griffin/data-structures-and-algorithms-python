# Challenge Summary
multi bracket validation

## Challenge Description
On your main file, create…

Python: a function called multi_bracket_validation(input)

Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Approach & Efficiency
create empty list for holding opening brackets -Queue

loop through each character ,i, in input
if the character is an opening br add it to the queue
if the character is a closing br
     if there is not a matching opening br
          return False
     if there is a matching opening bracket
          remove opening bracket form the list
if the list is empty return true
  (each opening br found a matching closing and was removed )
if the list is not empty return false (an opening br was added and was not removed with a match)


## Solution
![multi bracket validation whiteboard solution](/assets/multi_bracket_validation.png)
