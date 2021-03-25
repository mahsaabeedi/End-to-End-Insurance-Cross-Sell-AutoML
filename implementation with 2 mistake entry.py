# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:40:13 2019

@author: Mahsa
"""

import numpy as np
st=np.array([1, 1 ,1, -1])
st=np.reshape(st,(1,4))
s=np.reshape(st,(4,1))
w=np.multiply(s,st)

# =============================================================================
# input with one mistake
# =============================================================================
#st_disturb=np.array([-1, 1 ,1, -1])
# =============================================================================
# input with 2 mistake
# =============================================================================
st_disturb=np.array([-1, 1 ,-1, -1])
st_disturb=np.reshape(st_disturb,(1,4))
news=np.dot(st_disturb,w)
for i in range(4):
    if news[0,i]>0:
        news[0,i]=1
    else:
        news[0,i]=-1


i=np.identity(4)
w1=w-i
print(w1)
news=np.dot(st,w1)
for i in range(4):
    if news[0,i]>0:
        news[0,i]=1
    else:
        news[0,i]=-1