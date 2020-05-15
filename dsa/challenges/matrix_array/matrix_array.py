def matrix_array(arr):
  output_arr = [] # [ rowVal, rowVal] 
  for i in range(len(arr)):
    print(arr[i])
    counter = 0
    for j in range(len(arr[i])):
      counter += (arr[i][j])
    print(counter)
    output_arr.append(counter)
  print(output_arr)
  return output_arr

matrix_array([ [1,2,3], [4,5,6] ]) # [ 6, 15 ]

# def matrix_array(arr):
  # print(arr)
  # small_arr = []
  # for i in range(len(arr)): # [] [] []
    # small_arr.append[i]
    # print(arr[i])

    # for j in range(len(arr[i])): #small_arr: # [1,2,3]
      # add_arr = []
      # arr[i][0] = (arr[i][0] + arr[i][1])
      # print(arr[i][0])
      # print(arr[i][j])
      # print(arr[i][j])
      
      # small_arr = []
      # if j < in :
        # add = arr[0]+ arr[1]
        # small_arr.append(add)
      #   print(arr)
      # if j == len(arr)+1:
      #   break




# def matrix_array(arr):
  # for i in arr:
  #   print(arr[i])

# matrix_array( [ [1,2,3], [4,5,6] ] )



# arr = [ [1,2,3], [4,5,6], [7,8,9] ]
# print(arr[0])                   #[1,2,3]
# print(arr[0][0])                #1
# print(arr[0][0] + arr[0][1])    #1+2 = 3
# print(arr[0][0] + arr[1][2])    #1+5 = 7
