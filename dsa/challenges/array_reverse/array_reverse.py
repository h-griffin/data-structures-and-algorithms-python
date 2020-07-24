

def array_reverse(arr):
    return arr[::-1]


#
#   [ start : end ]
#
#   H  E  L  L  O
#   1  2  3  4  5
#  -5 -4 -3 -2 -1
#
#   [ 1 : 4 ] >>  E L L
#   [-4 : -1] >>  E L L
#
#
#
#  S[a:b:d]  third parameter specifies the step // 2everyother -1reverse
#
#   [ start : end : step ]
#
#   [::2]   >> H L O
#
#   [::-1]  >> O L L E H
#
