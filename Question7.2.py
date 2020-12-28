#Question 7.2(b)
#6-dimensional grid
#Write a code to convert given coordinates to index
import numpy as np
import pandas as pd
data=pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/input_coordinates_7_2.txt',sep='\t')
L=len(data.x1)
x1=np.array(data.x1)
x2=np.array(data.x2)
x3=np.array(data.x3)
x4=np.array(data.x4)
x5=np.array(data.x5)
x6=np.array(data.x6)
I=np.arange(L)

for i in range(L):
    I[i]=x1[i]+4*x2[i]+4*8*x3[i]+4*8*5*x4[i]+4*8*5*9*x5[i]+4*8*5*9*6*x6[i]
   
np.savetxt("C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/output_index_7_2.txt", I,fmt='%d',header='index',comments ='')

#Write a code to convert given index to coordinates
Index=np.array(pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/input_index_7_2.txt',sep='\t'))
length=len(Index)
X1=np.arange(length)
X2=np.arange(length)
X3=np.arange(length)
X4=np.arange(length)
X5=np.arange(length)
X6=np.arange(length)

for k in range(length):
    X6[k]=Index[k]//(4*8*5*9*6)
    X5[k]=(Index[k]-4*8*5*9*6*X6[k])//(4*8*5*9)
    X4[k]=(Index[k]-4*8*5*9*6*X6[k]-4*8*5*9*X5[k])//(4*8*5)
    X3[k]=(Index[k]-4*8*5*9*6*X6[k]-4*8*5*9*X5[k]-4*8*5*X4[k])//(4*8)
    X2[k]=(Index[k]-4*8*5*9*6*X6[k]-4*8*5*9*X5[k]-4*8*5*X4[k]-4*8*X3[k])//4
    X1[k]=Index[k]-4*8*5*9*6*X6[k]-4*8*5*9*X5[k]-4*8*5*X4[k]-4*8*X3[k]-4*X2[k]
    
Output=pd.DataFrame({'x1':X1,'x2':X2,'x3':X3,'x4':X4,'x5':X5,'x6':X6})
np.savetxt("C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/output_coordinates_7_2.txt", Output,fmt='%d',header='x1  x2  x3  x4  x5  x6',comments ='')
