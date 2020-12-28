#Question6
#Explanations
"""
When a line crosses a polygon boundary, there are only two cases: 
entering the polygon or passing through the polygon. 
Without considering the non Euclidean space, it is impossible for a straight 
line to enter the polygon again from the inside or pass through the polygon 
again from the outside, that is to say, the case of crossing the boundary 
twice in succession must be paired. 
The line can extend infinitely, but the area surrounded by the closed curve is 
limited, so the last time it crosses the polygon boundary, it must go out of 
the polygon and reach the outside.
As a result, if the point is inside the polygon, the ray must pass through the 
polygon for the first time; if the point is outside the polygon, the first time 
the ray crosses the boundary, it must enter the polygon. 
When the ray passes through the polygon boundary for an even number of times, 
all the even number of times (including the last time) passes through the polygon, 
so all the odd number of times (including the first time) passes through the polygon,
which can be inferred that the point is outside the polygon.
When the ray passes through the polygon boundary for an odd number of times, 
all the odd times (including the first time and the last time) pass through, 
so that we can infer that the point is inside the polygon.
"""
"""
A method of ray is implemented to this question:
Once make a ray, starting with the judgment point, in the right  
horizontal direction, and calculate the number of intersections between
the ray and each side of the polygon. If the number of intersections
is odd, the judgment point is inside the polygon, and if the number of
intersections is even, it is outside the polygon.
"""

    
import numpy as np
import pandas as pd
points=pd.DataFrame(pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 6/input_question_6_points.txt',sep='\t',header=None))
polygon=pd.DataFrame(pd.read_table('C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 6/input_question_6_polygon.txt',sep='\t',header=None))

points['x']=points[0].map(lambda x:x.split(' ')[0])
points['y']=points[0].map(lambda x:x.split(' ')[1])
points=points.drop([0],axis=1)
Tx=points['x'].astype(str).astype(int)
Ty=points['y'].astype(str).astype(int)
Tnum=len(points.x)
State=[]

polygon['x']=polygon[0].map(lambda x:x.split(' ')[0])
polygon['y']=polygon[0].map(lambda x:x.split(' ')[1])
polygon=polygon.drop([0],axis=1)
Px=polygon['x'].astype(str).astype(int)
Py=polygon['y'].astype(str).astype(int)
Pnum=len(polygon.x)
Px[Pnum]=Px[0]
Py[Pnum]=Py[0]

#The function determines whether the ray intersects with a line segment
def isIntersect(tx,ty,px,py,ppx,ppy):   
    if py==ppy:   #The situation that the ray is parallel, or coincident with one segment, or the starting and ending points of line segment are coincident
        return False
    if py>ty and ppy>py:   #The line segment is above the ray
        return False   
    if py<ty and ppy<ty:   #The line segment is under the ray
        return False
    if py==ty and ppy>ty:  #The intersection is the starting point of the line segment
        return False
    if ppy==ty and py>ty:  #The intersection is the ending point of the line segment
        return False
    if px<tx and ppy<ty:   #The line segment is to the left of the ray
        return False
    
    seg=ppx-(ppx-px)*(ppy-ty)/(ppy-py)   
    if seg<px:      #The intersection is to the left of the starting point of the ray
        return False
    return True    #Exclude above situations

innum=0
for i in range(Tnum):
    for k in range(Pnum):
        if isIntersect(Tx[i], Ty[i], Px[k], Py[k],Px[k+1], Py[k+1]):
            innum+=1
    if innum%2==1:
        State.append('outside')
    else: State.append('inside')

Output=pd.DataFrame({'Tx':Tx,'Ty':Ty,'State':State})
np.savetxt("C:/Users/Lenovo/Desktop/AY20_MBDS_questions/Question 6/output_question_6.txt", Output,fmt='%s')

            
            
            
             

    





