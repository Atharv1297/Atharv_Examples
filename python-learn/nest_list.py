# if __name__ == '__main__':
#     def Sort(sub_li):
#         l = len(sub_li)
#         for i in range(0, l):
#             for j in range(0, l-i-1):
#                 if (sub_li[j][1] > sub_li[j + 1][1]):
#                     tempo = sub_li[j]
#                     sub_li[j]= sub_li[j + 1]
#                     sub_li[j + 1]= tempo
#         return sub_li
    
#     list=[]
#     length=(int(input("length of list: ")))
#     for _ in range(length):
#         name = input("name : ")
#         score = float(input("score: "))
#         list.append([name,score])
    
#     list=Sort(list)
#     print(list[1][0])
