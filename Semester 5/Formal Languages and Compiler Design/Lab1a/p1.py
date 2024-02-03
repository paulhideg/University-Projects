#greatest number out of 3 numbers

var a
var b
var c
var maxi

rd (a) 
rd (b)
rd (c)

if (a > b)
    if (a > c)
        maxi = a 
    else 
        maxi = c
    
else if (b > c) 
        maxi = b
    else
        maxi = c

wr (maxi)