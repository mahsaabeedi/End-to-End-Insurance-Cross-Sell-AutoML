# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:25:05 2019

@author: Mahsa
"""

import numpy as np
st=np.array([1, 1 ,1, -1])
st=np.reshape(st,(1,4))
s=np.reshape(st,(4,1))
w=np.multiply(s,st)
print(w)
news=np.dot(st,w)
# =============================================================================
# apply activation function
# =============================================================================
for i in range(4):
    if news[0,i]>0:
        news[0,i]=1
    else:
        news[0,i]=-1

print(news)