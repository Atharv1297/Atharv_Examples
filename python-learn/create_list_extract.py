sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dict={}
for key in keys:
    dict.update({key: sample_dict[key]})
print (dict)