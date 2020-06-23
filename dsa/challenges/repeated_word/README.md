# problem domain
write a funtion that takes in a string and returns the first repeated word.

# edge cases
upper/lower case
punctuation

# big O

# algorithm
take in string
set empty list
set empty repeat variable
for word in string
    append to list
    if word in list
        word = repeat word
        break
return repeat word

# visual
input = 'it is dark, isn't it?.'
output = 'it'

'it is dark, isn't it?'
regex
'it is dark isnt it'
[ 'it', 'is', 'dark', 'isnt', it', ]
    ^
  [ 'it' ] ^
        [ 'it', 'is' ]   ^
             [ 'it', 'is', 'dark', 'isnt' ]

'it' in list = repeat word

[ 'it', 'is', 'dark', 'isnt', it', ]
    ^                          ^
repeat word = 'it'

![repeated word](assets/repeated_word.png)





