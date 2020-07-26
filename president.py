import panda_learning as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
data = pd.read_csv('/home/cyang/Downloads/PythonDataScienceHandbook/notebooks/data/president_heights.csv')
heights = np.array(data['height(cm)'])  # 身高

# print(heights)

print("Mean height: ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height: ", heights.min())
print("Maximum height: ",heights.max())

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()

print('done')
