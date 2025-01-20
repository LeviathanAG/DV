a=list(range(2,10,2))
for i in range(len(a)):
    print(i)

# List
a_list = [2, 3, 7, None]
print(a_list)
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
print(b_list)

# The list function iis frequently used in data processing as a way to materialize an iterator or generator expression
gen=range(10)
print(gen)
print(list(gen))

# Elements can be appended to the end of the list with the append method
a_list.append('dwarf')
print(a_list)

# Using insert you can insert an element at a specific location in the list
a_list.insert(1, 'red')
print(a_list)

# The insertion index must be between 0 and the length of the list, inclusive

# The inverse operation to insert is pop, which removes and returns an element at a particular index
a_list.pop()
print(a_list)

# Elements can be removed by value with remove, which locates the first such value and removes it from the last
a_list.append('foo')
print(a_list)
a_list.remove('foo')
print(a_list)

print(a_list.pop(2))


