def reverse(s):
	str = ""
	for i in s:
		str = i + str
		print(str)
	return str

s = "Geeksforgeeks"

print("The reversed string(using loops) is : ")
print(reverse(s))