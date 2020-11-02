
from matplotlib import pyplot as plt 
import numpy as np 
  
cars = ['AUDI', 'BMW', 'FORD', 
        'HONDA', 'HYUNDAI', 'MERCEDES' , 'SUZUKI', 'TATA'] 
  
data = [10, 13, 20, 27, 28, 12, 35 , 30] 

fig = plt.figure(figsize =(10, 7)) 
plt.pie(data, labels = cars) 

plt.show() 
