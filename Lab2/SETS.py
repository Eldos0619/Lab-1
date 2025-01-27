#Python Sets
#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#7
set1 = {"abc", 34, True, 40, "male"}
#8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access Set Items 
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Add Set Items
#1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Set Items
#1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Loop Sets
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
#1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#3
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
#5
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#6
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#7
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#8
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#9
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
#10
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
#11
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#12
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#13
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
#14
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
#15
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
#16
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Set Methods
"""
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""

