from dsa.data_structures.linked_list.linked_list import Node, Linked_list

def merge_lists( list1, list2):
    """takes two linked lists and merges them starting with head1 then head2"""
    if list1.head == None:
        return list2
    if list2.head == None:
        return list1

    list1_current = list1.head
    list2_current = list2.head
    merged = Linked_list()

    #checks is there are indexes available to merge
    while list1_current != None and list2_current != None:

        if list1_current != None:
            if merged.head == None:
                merged.insert(list1_current.value)
            else:
                merged.append(list1_current.value)

        if list2_current != None:
            if merged.head == None:
                merged.insert(list2_current.value)
            else:
                merged.append(list2_current.value)

        if list1_current and list1_current.next:
            list1_current = list1_current.next
        else:
            list1_current = False

        if list2_current and list2_current.next:
            list2_current = list2_current.next
        else:
            list2_current = False
    return merged
  
