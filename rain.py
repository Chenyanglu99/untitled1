import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

data = pd.read_csv('/home/cyang/Downloads/PythonDataScienceHandbook/notebooks/data/Seattle2014.csv')
rainfall = np.array(data['PRCP'].values)
inches = rainfall / 254

print(inches.shape)

plt.hist(inches, 40)

rainy = (inches > 0)

# 构建一个包含整个夏季日期的掩码（6月21日是第172天）  
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)

print('median precip on rainy days in 2014 (inches): ', np.median(inches[rainy]))

print("Median precip on summer days in 2014 (inches): ", np.median(inches[summer]))

print("Maximum precip on summer days in 2014 (inches): ", np.max(inches[summer]))

print('Median precip on non-summer rainy days in 2014 (inches): ', np.median(inches[rainy & ~summer]))
