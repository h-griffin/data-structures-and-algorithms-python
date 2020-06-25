# problem domain
write a function that takes in two hashmaps and left joins into one
datastructure.

hashmap1 = 'word string key':'synonym of key as value'
hashmap1 = 'word string key':'antonym of key as value'




LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.


input
1 synonym table = ['fond':enamored, 'wrath':anger]
2 antonym table = ['wrath':anger, 'wrath':delight]

output = [ key, 1, 2]
[
    ['fond', 'enamored', 'averse'],
    ['wrath', 'anger', 'delight'],
]

