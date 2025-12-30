import numpy as np
import pandas as pd
import matplotlib.patches as plt

# print("np.__version__", np.__version__)
# print("pd.__version__", pd.__version__)
# print("OK")

num_list = [1,2,3,4,5]
print(num_list) 
data = np.array(num_list) #넘파이 array > 여러가지 집계 함수가 포함되어있다
print(data)

print(data.mean())
print(data.max())