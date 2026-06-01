## 5.	WAP to display a user entered name followed by Good Afternoon using input() function.
# name = input("Enter your name: ")
# print("Good Afternoon", name)



## 6.	Wap to detect double space in a string.
# str = input("Enter a string: ")
# if "  " in str:
#     print("double space is detected")
# else:
#     print("No double space found")



## 7.	Replace double space with single space
# str = input("Enter a string: ")
# a = str.replace("  ", " ")
# print(a)



## 8.	WAP to store 7 fruits in a list entered by the user.
# fruits = []
# for i in range(0, 7):
#     fruit = input("Enter fruit {i+1}: ")
#     fruits.append(fruit)
# print("Fruits list:", fruits)



# # 9.	WAP to accept marks of 6 students and display them in a sorted manner.
# marks = []
# for i in range(6):
#     m = input("Enter your marks: ")
#     marks.append(m)
#     marks.sort()
# print(marks)



# 13.	WAP to create dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!.
dict_hindi = {
    "namaste": "hello",
    "paani": "water",
    "kitab": "book",
    "ghar": "home",
    "dost": "friend"
}
word = input("Enter a Hindi word: ")
if word in dict_hindi:
    print("English meaning: ", dict_hindi[word])
else:
    print("Word not found in dictionary")