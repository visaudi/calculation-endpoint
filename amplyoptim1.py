from gurobipy import *
import numpy as np

# v = no of vehicles, n = time intervals, i vehicles, j intervals
v = 10; n = 10; interval = 24.0/n; MaxP = 20; SOC = 4;
d = {'MaxP': MaxP, 'SOC': SOC}

def kwH_rate (t):
    if (0 <= t < 9) or (22 <= t < 24):
        result = 20
    if 9 <= t < 14:
        result = 10
    if 14 <= t < 22:
        result = 30
    return result

c = [0 for j in range(n)]
slots =[j*interval for j in range(n)]

for j in range(n):
        c[j] = kwH_rate(j*interval)
        
m = Model()

# Add variables
p = {}
p = m.addVars(v,n,name='p')

m.update()

# Add constraints
for j in range(n):
    m.addConstr(quicksum(p[i,j] for i in range (v)) <= MaxP)

for i in range(v):
    m.addConstr(quicksum(p[i,j] for j in range (n)) >= SOC)
    
# Set objective
m.setObjective(quicksum(p[i,j] * c[j] for i in range (v) for j in range(n)), GRB.MINIMIZE)
        
m.optimize()

for i in range(v):
    for j in range(n):
         p[i,j] = p[i,j].X
    
print('Obj:', m.objVal)

import pandas as pd

#for k in p.keys():   
    #print("Got key", k, "which maps to value", p[k])
#    print(p.keys().index(k))

#Matrix = [[1 for x in range(n)] for y in range(v)] 
Matrix = [[p[i,j] for j in range(n)] for i in range(v)]
df1 = pd.DataFrame(Matrix)
df1.columns = slots
df2 = pd.DataFrame(d, index = ['Constraints'])
df3 = pd.DataFrame(c, index = slots)

df1.to_json(orient='index')
df1.to_json('amplyoptim1_Matrix.txt')

#df = pd.DataFrame(data=p.items()) 

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()



#E[i,j] = p[i,j] * 




#Minimize
#  2 p11 + p12 + p13 + 2 p21 + p22 + p23
#Subject To
#  SOC1: p11 + p12 + p13 >= 2
#  SOC2: p21 + p22 + p23 >= 2
#  MaxP: p11 + p21 <= 2
#  MaxP: p12 + p22 <= 2
#  MaxP: p13 + p23 <= 2
#Integers
#  p11 p12 p13 p21 p22 p23 
#End
