
# Approach 1

word = input("Enter The Word: ")
#word = "ganga dhar hyd"
z = list(word)
y = z[::-1]
word = ''.join(y)
print(word)