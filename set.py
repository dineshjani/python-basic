firstset = {"Johnny", "Nilanjan", "Rupa"}
firstset.add("Sepoy")
print(firstset)
firstset.add("Nilanjan")
firstset.add("Sepoy")

A1= {24, 35, 34, 45}
A2= {24, 56, 35, 46}
print(A1.difference(A2))
print(A2.difference(A1))

A1= {24, 35, 34, 45}
A2= {24, 56, 35,45, 46}
A3= {24, 35, 47,45, 56}
A4= {24, 56, 35,45, 46}
#remove throw error but discard does not throw error if element is not present in set
print(A1.intersection(A2, A3,A4))
firstset = {"Johnny", "Nilanjan", "Rupa"}
firstset.discard("Nilanjan")
print(firstset)
firstset.discard("Rocky")
print(firstset)
#symmetric_difference not part of both set
Veggie_set1 = {"Cabbage","Cauliflower","Kale"}
print(Veggie_set1)
Veggie_set2 = {"Cauliflower","Cabbage","Lady-finger"}
print(Veggie_set2)
check = Veggie_set2.symmetric_difference(Veggie_set1)
print(check)

#This method helps update a set with the element that is part of other specified sets but not of this set.
Veggie_set1 = {"Cabbage","Cauliflower","Kale"}
print(Veggie_set1)
Veggie_set2 = {"Cauliflower","Cabbage","Lady-finger"}
print(Veggie_set2)
Veggie_set2.update(Veggie_set1)
print(Veggie_set2)