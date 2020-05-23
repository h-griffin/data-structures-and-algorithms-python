def mergeLists( list1, list2):
    list1_current = list1.head
    list2_current = list2.head

    #checks is there are indexes available to merge
    while list1_current != None and list2_current != None:

        list1_next = list1_currrent.next
        list2_next = list2_current.next

        list2_current.next = list1_next
        list1_current.next = list2_current

    other_list.head = list2_current

    #find list 1 head
    #change next value to list 2 head
    #change list2.head next value to list 1.head origional next