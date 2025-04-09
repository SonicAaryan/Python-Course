# Elements can't be repeated
# To create empty set do this -> emptySet = set() # Don't print empty set

set={1, 2, 4, 6 ,6} 
set.add(7)
print(set) 
print(len(set)) 

'''
Properties :
    1) Set are unordered => Element's order doesn't matter
    2) Sets are unindexed => Cannot access elements by index
    3) There is no way to change items in sets.
    4) Sets cannot contain duplicate values.
'''
s1 = {1,45, 7}
s2 = {0,20, 7}
print(s1.union(s2)) 
print(s1.intersection(s2)) #Give's common  value.

'''
 Methods : 
           len(set): Returns 4, the length of the set
           set.remove(8): Updates the set and removes 8 from set.
           set.pop(): Removes an arbitrary(Random) element from the set and return the element removed.
           set.clear():empties the sets.ff
           set.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
           set.intersection({8,11}): Return a set which contains only item in both sets {8}.
'''