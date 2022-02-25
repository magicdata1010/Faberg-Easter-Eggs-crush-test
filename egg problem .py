# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:15:52 2022

@author: 91838
"""
for i in range(8): # filling dp rows
   dp[1,i]=i
print(dp[1][-8])
g=[]
for i in range(4): # filling dp cols
    dp[i,1]=1
for i in range(2,4): # filling other dp values to find the result
    for j in range(2,8):
        b=j-1
        for k in range(j):
            f=sys.maxsize**10
            print(k,"hh")
            #b=j-1 # using other variables to iterate thru 
            
            
            
            
            g.append(max(dp[i-1][k],dp[i][b]) )#finding values using bottom uo dp method 
            b=b-1
            #g.append(s)
            print(b,g,"pp")
            f=min(g)
            print(f,"yyY")
        #f=min(g)
        dp[i,j]=f+1
        
        g.clear()# clearing the list
print(dp)     



