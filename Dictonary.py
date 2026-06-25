#dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

dict ={
    "name": "John",
    "age": 30,  
    "cgpa": 3.5,
    "marks": [90, 85, 92]
}

print(dict)   
print(type(dict))  
print(dict["name"])
print(dict["age"])
print(dict["cgpa"])
print(dict["marks"])

dict["name"] = "Priyanshu"
dict["surname"] = "Kumar"
print(dict)



#null dictionary 
nullDict = {}
print(nullDict)



#nested dictionary
nestedDict = {  
    "child1": {
        "name": "Emil",
        "year": 2004,
        "subject":{
            "math": 95,
            "science": 88
        }
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    }
}
print(nestedDict)
print(nestedDict["child1"]["subject"]["math"])  # Output: 95
print(nestedDict["child1"]["subject"]["science"])  # Output: 88


#dictionary methods
dict1 = {
    "name": "John",
    "age": 30,
    "cgpa": 3.5
}
print(dict1)
print(dict1.keys()) 
print(dict1.values())
print(dict1.items())# Output: John
print(dict1.update({"age": 31}))
print(dict1)  

