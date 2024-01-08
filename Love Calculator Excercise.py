#Love Calculator
name = input("enter your first name ").lower()
name_2 = input("enter your first name ").lower()

t= name.count("t")
r= name.count("r")
u= name.count("u")
e= name.count("e")

l= name.count("l")
o= name.count("o")
v= name.count("v")
e_1= name.count("e")

total = (t+r+u+e +l+o+v+e_1)

t_1= name_2.count("t")
r_2= name_2.count("r")
u_2= name_2.count("u")
e_2= name_2.count("e")

l_2= name_2.count("l")
o_2= name_2.count("o")
v_2= name_2.count("v")
e_2= name_2.count("e")

total_2 = (t_1+ r_2+u_2 +e_2 + l_2+o_2+v_2+e_2)
total_score = str(total) + str(total_2)
print(total_score)
