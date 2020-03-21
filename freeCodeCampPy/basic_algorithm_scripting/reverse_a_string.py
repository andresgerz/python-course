"""
Basic Algorithm Scripting: Reverse a String

Reverse the provided string.
You may need to turn the string into an array before you can reverse it.
Your result must be a string.
Remember to use Read-Search-Ask if you get stuck. Write your own code.
"""



#def reverse_string(string):
string = "idish"
list = []

for i in range(len(string)-1, -1, -1):
    
    list.append(string[i])
    
s = ""    

for i in list:
    s += i

print(s)
