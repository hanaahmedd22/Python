# Write a Python program to reverse a string. 
s1="Hello"
print (s1[::-1])

#Write a Python program to check if a string is a palindrome (reads the same backward as forward). 
s1="yoy"
print (s1==s1[::-1])

#Write a Python program to remove duplicate characters from a string.
s1="hello"
print ("".join(set(s1)))


#Write a Python program to find the longest word in a given string. 
text = "Python is a great programming language" 
print (max(text.split(" "), key=len))

#Write a Python program to find common elements between two tuples. 
tuple1 = (1, 2, 3) 
tuple2 = (2, 3, 4) 
print (set(tuple1) & set(tuple2))#intersection  

#Write a Python program to find the maximum and minimum value in a dictionary. 
my_dict = {"a": 10, "b": 20, "c": 5} 
print (max(my_dict.values()))
print (min(my_dict.values()))

#Write a Python program to merge two dictionaries.
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4}
print({**dict1, **dict2})

#Write a Python program to find common keys in two dictionaries. 
dict1 = {"a": 1, "b": 2, "c": 3} 
dict2 = {"b": 2, "c": 4, "d": 5} 

print (set(dict1.keys()) & set(dict2.keys()))

#Takes a string and prints the longest alphabetical ordered substring occured. 
s = 'abdulrahman'
s=s.lower()
long=""
for i in range(len(s)):
    if ord(s[i]) > ord(s[i+1]):
        long+=s[i]
        break
    else:
        long+=s[i]
print(long)
        