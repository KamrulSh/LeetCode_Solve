# Using set
```
set1 = set(nums1)
set2 = set(nums2)
set3 = set(nums3)
​
# Set Intersection
ints1 = set1 & set2
ints2 = set1 & set3
ints3 = set2 & set3
​
# Set union
uni = ints1 | ints2 | ints3
return uni
```
​
# using hashtable
```
table = {}
for i in nums1:
if i not in table:
table[i] = {1}
​
for i in nums2:
if i not in table:
table[i] = {2}
else:
table[i].add(2)
​
for i in nums3:
if i not in table:
table[i] = {3}
else:
table[i].add(3)
​
li = []
for i in table:
if len(table[i]) >= 2:
li.append(i)
return li
```