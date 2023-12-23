#Write a program that asks me my weight
# It then asks the weight whether it's in kgs or lbs( write kgs/lbs)
weight = int(input("weight: "))
measure = input( "(K)g's or (L)bs:  ")
if measure.upper() =="K":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs: " + str(converted))
