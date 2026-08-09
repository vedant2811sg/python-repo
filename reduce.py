from functools import reduce
numbers=[1,2,3,4,5]
sum_of_nos=reduce(lambda acc, x: acc+x,numbers)
max_values=reduce(lambda acc, x: acc if acc>x else x,numbers)
