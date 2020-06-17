# merge sort
![origional](/assets/blog-merge-assets/origional-sorted.png)


1 - split array into two halves
![step1](/assets/blog-merge-assets/step1.png)

2 - create two variables to traverse each half at the same time (i & j) and create one to iterate the whole list adn make changes along the way (k) (values assigned to k are sorted)

3 - compare left and rights, in this case each righ tis less than the left, so they switch places.
![step2](/assets/blog-merge-assets/step2.png)

4 - compare the last value, in this case both last values are the largest value, so they go on the right.
![step3](/assets/blog-merge-assets/step3.png)

5 - here we begin to merge the two halves back together. sort each new value from the right into the left until both lists are megered back together into one.
![step4](/assets/blog-merge-assets/step4.png)
