num = float(input("Enter the number:"))
print("Chose between F & C")
print("The letter that you will enter will determine what is the previous number")
way = str(input("Enter the letter please:"))
if way == "F" :
    print(((num -32)/ 1.8), " C")
if way == "C":
    print(((1.8*num)+32), " F")
    

          
