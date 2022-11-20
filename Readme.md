# Homework Description

Write a program in Python including the following:

- A function that takes an integer and forms a list of its digits.
  
  - Sample Run:
    x=239945
    lst=fun(x)
    [2, 3, 9, 9, 4, 5]

- A function which takes a list of integer digits, and an integer y (1-digit) as parameter, 
  and performs the following:
  
  - If the list is of even length, replaces the maximum number of the list with y. If 
    the maximum number occurs more than once, replace all.
  
  -  If the list is of odd length, insert as many y’s as the length of the list, to the 
    front of the list.
  
  - Print the resulting list.
    
    - Sample Run:
      form(lst,1) #for lst=[2,3,9,9,4,5]
      [2,3,1,1,4,5]
      form(lst,1) #for lst=[2,3,4]
      [1,1,1,2,3,4]

-  Read 2 integers x and y (y should be 1-digit), call the first function with x, and send 
  the resulting list, and y to the second function. Lastly, print the resulting list.
  
  <b>Restrictions: You can use list functions, but no loops and no type conversion. Recursion is allowed.</b>


