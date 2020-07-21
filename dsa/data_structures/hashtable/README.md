# hashtable

## description & Big O
uses a linked list and a hashmap to store data with an O(1) lookup time, worst case O(N), in regards to collisions, in which two inputs have the same key but different values, these key:value pairs are stored in a linked list at the hashtable index. O(N) is worst case the length of the longest linked list index/bucket.


## visual
![hashtable](assets/hashtable.png)

### Features
Implement a Hashtable with the following methods:

- add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get: takes in the key and returns the value from the table.
    contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
- hash: takes in an arbitrary key and returns an index in the collection.

Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

Adding a key/value to your hashtable results in the value being in the data structure
Retrieving based on a key returns the value stored
Successfully returns null for a key that does not exist in the hashtable
Successfully handle a collision within the hashtable
Successfully retrieve a value from a bucket within the hashtable that has a collision
Successfully hash a key to an in-range value
Ensure your tests are passing before you submit your solution.
