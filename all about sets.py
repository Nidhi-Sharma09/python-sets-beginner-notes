#sets are unordered collections of unique elements they do not follow a specific order and they do not allow duplicate values
#sets are mutable that mean we can add remove elements from a set as per our requirement
#sets are defined using curly braces {} or the set() constructor
#see dictionary also uses curlyt braces but in dictionary we can pair key and its values


#creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set) #output: {1, 2, 3, 4, 5}
print(type(my_set)) #output: <class 'set'>


#how sets do not allow duplicate values
my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set) #output: {1, 2, 3, 4, 5} so bacically it will ignore the duplicate values and only keep one instance of each unique value like it kept 5 only for one time


#adding elements to a set
my_set.add(6)
print(my_set) #output: {1, 2, 3, 4, 5, 6}


#removing elements from a set
my_set.remove(3)
print(my_set) #output: {1, 2, 4, 5, 6}
#discard method is used to remove an element from a set if it is present in the set if the element is not present in the set it will not raise an error


#popping an element from a set it is fifo method if we dont mention which element to pop it will pop the first element 
popped_element = my_set.pop()
print(popped_element) #output: 1 (it will remove and return an arbitrary element from the set)
print(my_set) #output: {2, 4, 5, 6}


#checking if an element is in a set
print(4 in my_set) #output: True
print(3 in my_set) #output: False


#mathamatical operations on sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#union of sets
union_set = set_a.union(set_b)
print(union_set) #output: {1, 2, 3, 4, 5, 6} it will combine all the unique elements from both sets


#intersection of sets
intersection_set = set_a.intersection(set_b)
print(intersection_set) #output: {3, 4} it will return the common elements between both sets


#difference of sets
difference_set = set_a.difference(set_b)
print(difference_set) #output: {1, 2} it will return the elements that are present in set_a but not in set_b


#symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set) #output: {1, 2, 5, 6} it will return the elements that are present in either set_a or set_b but not in both sets


#subset and superset
#is subset
print(set_a.issubset(set_b)) #output: False because set_a is not a subset of set_b as it contains elements that are not present in set_b
#is superset
print(set_a.issuperset(set_b)) #output: False because set_a is not a superset of set_b as it does not contain all the elements of set_b
# only if set_a contains all the elements of set_b then it will be a superset of set_b 
# if set_b contains all the elements of set_a then it will be a subset of set_a


#removing duplicates from sets using sets
numbers={1,2,2,3,4,5,5,5,6,7,8,8}
removed_duplicates = set(numbers)
print(removed_duplicates) #output: {1, 2, 3, 4, 5, 6, 7, 8} it will remove the duplicate values from the list and return a set of unique values


