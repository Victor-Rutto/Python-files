# TUPLES
#They store sequence of data/items
# They are immutable/Unchangable
tuple_1 = (1, 2, 4, 6, 61, 'HERRY', 'Victor', 0.3)
tuple_2 =(10,)

# print(tuple_1[1])
# print(tuple_1[-2])
# print(type(tuple_1))
# tuple_1[0]= 30 # This gives an error.. Tuples dont change

# print(tuple_1[0:])
# print(tuple_1[::2])
# print(len(tuple_1))

tuple_3 = (tuple_1, tuple_2)
# print(tuple_3)
# print(len(tuple_3))
tuple_4 = tuple_3 +tuple_2
# print(tuple_4)

#Converting list to a tuple
list1= [1,2, 3, 4]
tuple5=(tuple(list1))
# print(tuple5)
# print(len(tuple5))
tuple6=(13, 80, 80)*5
print(tuple6)


