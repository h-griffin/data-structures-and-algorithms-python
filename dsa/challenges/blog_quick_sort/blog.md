## quick sort

![origional](assets/blog-quick-sort-assets/origional.png)

![step 1](assets/blog-quick-sort-assets/step1.png)

1 - itterate though the list and find the pivot, the left most unsorted value, in this case it is 8

![step2](assets/blog-quick-sort-assets/step2.png)
2 - begin the partition and itterate through, checking if the value is less than or greater than 8. the sorted values are now 4 and 8

3 - begin another itteration or partition through with the new pivot, 23. check for values less than 23, in this case 15 and 16. becase 15 and 16 are less than 23, but 42 is greater, it it takes that spot.

![step3](assets/blog-quick-sort-assets/step3.png)
4 - partition one last time with the lowest unsorted value (pivot) which is 16, 15 is less than 16 so they swap places. the list is now sorted



