import json

json_obj = json.dumps({"a": [1,2]})
json_obj1 = json.dumps({"a": [3,4]})

print(type(json_obj1))  # the type is `str`

json_obj += json_obj1   # this concatenates the two str objects

json_obj = {"a": [1,2]}
json_obj1 = {"a": [3,4]}

json_obj["a"].extend(json_obj1["a"])
 
print(json_obj)