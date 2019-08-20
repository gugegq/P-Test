'''
Created on 2019年8月5日

@author: qiao.gu
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
from pandas import Series,DataFrame

s1=Series(np.random.randn(1000))
sns.distplot(s1,hist=True,kde=True)