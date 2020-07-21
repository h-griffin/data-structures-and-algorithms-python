# problem domain
write a function that takes in two hashmaps and left joins into one
datastructure.

LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.


hashmap1 = 'word string key':'synonym of key as value'
hashmap1 = 'word string key':'antonym of key as value'


input
1 synonym table = ['fond':enamored, 'wrath':anger]
2 antonym table = ['fond':averse, 'wrath':delight]

output = [ key, 1, 2]
[
    ['fond', 'enamored', 'averse'],
    ['wrath', 'anger', 'delight'],
]

algorithm
set empty output list
for each key in 1
    append key:value pair
    check if 2 has key
        TRUE append value
        FALSE append none
    append row to output
return output

![left join](assets/left_join.png)

### Feature Tasks
Write a function that [LEFT JOINs](https://www.tutorialspoint.com/sql/sql-left-joins.htm) two hashmaps into a single data structure.
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
Avoid utilizing any of the library methods available to your language.
Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write at least three test assertions for each method that you define.

Ensure your tests are passing before you submit your solution.

Example
![input-output](assets/left_join_inout.png)

Stretch Goals
Consider a RIGHT JOIN. Can you implement this as a new function? How about by passing an optional parameter to your initial function, to speficy if LEFT JOIN or RIGHT JOIN logic should be used?
