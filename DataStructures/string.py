str1= "This is a string"
str2 ="Priyanshu"
print(str1)
print(str2)

#string concatenation
str3 = str1 + " " + str2
print(str3)

#length
print(len(str1))
print(len(str2))

#string indexing
print(str1[0])  # T
print(str1[5])  # i 
print(str1[-1]) # g 
print(str1[-2]) # n
print(str1[0:4])  # This
print(str1[2])  # i
str1 = str1[:2] + "Z" + str1[3:]
print(str1)
print(str1[1:6])  # hZs i
print(str1[-5:-1])  # trin  #slicing
print(len(str1))  # 16



str = "i am learning python"
print(str.endswith("python"))  
print(str.startswith("i am"))
print(str.find("learning"))  # 5
print(str.count("n"))  # 2
print(str.replace("python", "java"))  # i am learning java
print(str.upper())  # I AM LEARNING PYTHON
print(str.capitalize())  # I am learning python
print(str.lower())  # i am learning python
print(str.replace("n","m"))  # i am learmimg python
print(str.find("a"))  # 2
print(str.find("j"))  # -1