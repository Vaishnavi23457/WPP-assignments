
print("equivalance class for 1-10000")
list0 = [i for i in range(1,10001) if i%5==0]
list0=set(list0)
list1 = [i for i in range(1,10001) if i%5==1]
list1=set(list1)
list2 = [i for i in range(1,10001) if i%5==2]
list2=set(list2)
list3 = [i for i in range(1,10001) if i%5==3]
list3=set(list3)
list4 = [i for i in range(1,10001) if i%5==4]
list4=set(list4)
# Check if the union of all equivalence classes is equal to the original set
all_numbers = set(range(1, 10001))
union_of_classes = list0.union(list1, list2, list3, list4)
if union_of_classes == all_numbers:
        print("Equivalence class for 1- is Valid")
else:
        print("Equivalence class for 1-10000 is Invalid")
10000

