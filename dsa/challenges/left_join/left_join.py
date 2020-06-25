def left_join(hashmap1, hashmap2):
    """Takes in two hash maps, and returns a left joined combination of both tables"""
    output = []

    for key in hashmap1: # 1 left
        row = []
        row.append(key) # key
        row.append(hashmap1[key]) # synonym value

        try:
            if hashmap2[key]: # 2 right
                row.append(hashmap2[key]) # antonym value
        except:
            row.append(None)

        output.append(row) # adds row results to the output list
    return output
