name=input("Enter Student Name: ")

math=int(input("Enter math marks: "))
physics=int(input("Enter physics marks: "))
chemistry=int(input("Enter chemistry marks: "))
english=int(input("Enter english marks: "))

totalmarks=math+physics+chemistry+english
average=totalmarks/4

print("\nStudent Name:",name)
print("totalmarks:",totalmarks)
print("average:",average)

if average>= 80:
    print("Grade: A+")
elif average>= 70:
    print("Grade: A")
elif average>= 60:
    print("Grade: A-")
elif average>= 50:
    print("Grade: B")
elif average>=40:
    print("Grade: C")
elif average>=33:
    print("Grade: D")
else:
    print("Grade: F")
print("Thank you !")
