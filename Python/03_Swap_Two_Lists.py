
A = input("Enter List of Variables A: ")
B = input("Enter List of Variales B: ") 

a_list = A.split(' ')
b_list = B.split(' ')

print("before Swapping Lists")
print(a_list)
print(b_list)

if len(a_list) != len(b_list):
    print("List are not equal")
else:
    for i in range(len(a_list)):
        a_list[i], b_list[i] = b_list[i], a_list[i]


print("After Swapping Lists")
print(a_list)
print(b_list)