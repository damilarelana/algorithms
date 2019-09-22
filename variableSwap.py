*Recommendation*
Avoid the over-use of coding tricks. As some so called `coding tricks` can actually make debugging more difficult down the line [if we use them in scenarios where they are not appropriate]

*Example*
Two variables (`x` and `y`) can be swapped using the following approaches below:

`Method 1`
temp = x
x = y
y = temp

`Method 2`
x = x + y
y = x - y
x = x - y

`Method 3`
x = x ^ y
y = x ^ y
x = x ^ y

*Observation*:
`method 1` uses a temporary throw-away variable
`method 2` and `method 3` avoid the use of a temporary throw-away variable
`method 3` can lead to debugging issues, for the scenario where the two variables point to same memory location:
    - causing `XOR` to zero out your variables
    - aka `aliasing` problem

*Ref*
https://en.wikipedia.org/wiki/XOR_swap_algorithm
https://en.wikipedia.org/wiki/XOR_gate
https://betterexplained.com/articles/swap-two-variables-using-xor/
https://en.wikipedia.org/wiki/Aliasing_%28computing%29
