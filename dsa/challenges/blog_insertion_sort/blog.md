# insertion sort

## pseudo code
``` InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## description
![origional-sorted](/assets/blog-assets/origional-sorted.png)
insertion sort looks though the list/array and temporarily removes the second index, storing it in a value. this leaves a gap for the list to be modified and moved. each loop through the array will remove and store each index value at its cooresponding loop, (loop 1 = index 1, loop 2 = index 2, loop 3 = index 3 ...) this leaves a value to the left and right of the stored value.

remove index 1 and compare that value to index 0
        if the left is greater than the value then shift it to the right and place the value in the new gap on the left (the the left value of the gap is still less, continue moving the value to the right)

## steps
![step 1](/assets/blog-assets/step1.png)
1 - remove index 1 and compare that value to index 0
        because 8 is greater than 4, we move 8 to the right and fill the gap, then put for into the new gap where 8 used to be (idx 0)

![step 2](/assets/blog-assets/step2.png)
2 - remove index 2 and compare that value to index 1
        because 4 is less than/ not greater than 8, 8 goes back into its spot. no shifting has occured in this loop


![step 3](/assets/blog-assets/step3.png)
3 - remove index 3 and compare that value to index 2
        because 8 is less than/ not greater than 23, 23 goes back into its spot. no shifting has occured in this loop

![step 4](/assets/blog-assets/step4.png)
4 - remove index 3 and compare that value to index 2
        because 23 is less than/ not greater than 42, 42 goes back into its spot. no shifting has occured in this loop


![step 5](/assets/blog-assets/step5.png)
5 - remove index 4 and compare that value to index 3
        because 42 is greater than 16, 42 moves to the right filling teh gap/idx 16 used to hold. then because the left of this gap is still greater than the value, 23 is greater than 16. so it also moves to the right and takes the place 42 used to hold. then because 8 is not greater than 16, it takes the place of the gap, where 23 used to be.

![step 6](/assets/blog-assets/step5.png)
6 - remove index 5 and compare that value to index 4
        because 42 is greater than 15 it moves right, 23 is greater than 15 so it also moves right, and then 16. 15 takes the gap that 16 used to hold. 

