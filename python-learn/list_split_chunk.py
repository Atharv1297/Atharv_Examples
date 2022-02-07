list=[1,2,3,4,5,7,8,5,6,14,25,36,78,25,36]
limit_chunk=4
gapping=0
new_gapping=limit_chunk

while gapping < len(list) & new_gapping <= len(list):     
    
    print(list[gapping:new_gapping])
    
    gapping+=limit_chunk
    
    new_gapping+=limit_chunk
        
    
        
