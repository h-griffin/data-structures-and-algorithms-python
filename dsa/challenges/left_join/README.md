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
