#Question 7.1(b)
#2-dimensional grid
#Write a code to convert given coordinates to index
import numpy as np
import pandas as pd
data=pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/input_coordinates_7_1.txt',sep='\t')
L=len(data.x1)
x1=np.array(data.x1)
x2=np.array(data.x2)
I=np.arange(L)

for i in range(L):
    I[i]=x1[i]+50*x2[i]
   
np.savetxt("C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/output_index_7_1.txt", I,fmt='%d',header='index',comments ='')

#Write a code to convert given index to coordinates
Index=np.array(pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt',sep='\t'))
length=len(Index)
X1=np.arange(length)
X2=np.arange(length)

for k in range(length):
    X2[k]=Index[k]//50
    X1[k]=Index[k]-50*X2[k]
    
Output=pd.DataFrame({'x1':X1,'x2':X2})
np.savetxt("C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/output_coordinates_7_1.txt", Output,fmt='%d',header='x1   x2',comments ='')