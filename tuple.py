# a tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

tup = (4,5,6),(6,7,8)
print(tup)
tup1=tuple("string")
print(tup1)
print(tup1[0])
print(tup1[1])
tup2=tuple(['foo',[1,2],True])           
print(tup2)
tup2[1].append(3)
print(tup2)
# if an object inside a tuple is mutable, such as a list, you can modify it in-place.

# You can concatenate or multiply tuples

tup3=tup1+tup2
print(tup3)

tup4=tup1*3
print(tup4)

# You can unpack a tuple into several variables
a,b=tup
print(a)

# We can swap variables 
a,b=1,2
b,a=a,b
print(a)
print(b)

# A common use of variable unpacking is iterating over sequences of tuples or lists
seq=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0},b={1},c={2}'.format(a,b,c))



# You can use the *rest syntax to capture an arbitrarily long list of positional arguments
values=1,2,3,4,5
a,b,*rest=values
print(a)
print(b)
print(rest)

# Tuple Methods
# Since the size and contents of a tuple cannot be modified, it is very light on instance methods.
# A particularly useful one (also available on lists) is count, which counts the number of occurrences of a value
a=(1,2,2,2,3,4,2)
print(a.count(2))



