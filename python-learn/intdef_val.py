employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict={}
for i in employees:
    dict.update({i:defaults})
print(dict)