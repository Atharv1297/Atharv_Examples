w_list=["joint","for","its"]
list2=["venture","tomey","good"]
for i in w_list:
    ind_l1=w_list.index(i)
    for j in list2:
        ind_l2=list2.index(j)
        if ind_l1==ind_l2:
           print(i, j)