import json

# Person = {
#  'Name' : "Allan Smith",
#  'Man': True,
#  "age" : 45,
#  'siblings': ["Yae","Samuel","Liz","Ammon"],
#  "Pet" : None
# }
# print(Person)
# print("Datatype before conversion: ",type(Person))
# json_string = json.dumps(Person)
# print(json_string)
# print("Datatype after conversion", type(json_string))


# initializing string  
string1 = '{"Kiprono" : 67, "Bob" : 76, "Alice" : 88}' 
  
# printing original string  
print(string1)
print ("Type before converting:",type(string1)) #check type
  
# convert dictionary string to dictionary 
res = json.loads(string1)
  
# print result 
print(res) 
print("Type after converting: ",type(res)) #check type

# ----------Output----------
# {"Kiprono" : 67, "Bob" : 76, "Alice" : 88}
# Type before converting: <class 'str'>
# {'Kiprono': 67, 'Bob': 76, 'Alice': 88}
# Type after converting:  <class 'dict'>