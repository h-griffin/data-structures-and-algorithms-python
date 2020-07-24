# Challenge Summary
First-in, First out Animal Shelter.

## Challenge Description
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Approach & Efficiency
create a stack called kennel, and a temporary list to hold the object /animal. when adding an animal to the kennel, print hte added animal to the list. when removing an enimal from the kennel, check if it is a cat or a dog, if it is not return none, if it is a cat or a dog check if the first animal in the kennel matches what was asked to take out. if it is, take out the animal, and print the animals left in the kennel. if the first animal in the kennel is not what was asked for, move the animals into the temporary list until the first animal is the one that wasa asked for. once it is, pop that animal and save to a variable, starting from the end of the temp list push the animals back into kennel to reserve the order of the stack. return the animal that was removed from the kennel.errrr

## Solution
![fifo animal shelter solution](/assets/fifo-animal-shelter.png)


### help from James Salomonsen


### Feature Tasks
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

Stretch Goal
If a cat or dog isn’t preferred, return whichever animal has been waiting in the shelter the longest.

Requirements
Ensure your complete solution follows the standard requirements.

Write [unit tests](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Testing)
Follow the [template for a well-formatted README](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Documentation)
Submit the assignment following [these instructions](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Challenge_Submission)
