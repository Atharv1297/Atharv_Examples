keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict={}
for i,j in zip(keys, values):
    dict.update({i:j})
print(dict)