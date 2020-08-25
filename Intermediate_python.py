# Using Matplotlib

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')
plt.yticks([0,....],['0B,....'])

plt.show()

# other options are a scatter plot

import matplotlib.pyplot as plt
plt.hist(x, bins =) #x is the list of values
plt.show()

D#ictionaries

Consider this example to find the population in two different lists.
pop = [30.55, 2.77, 39.21]
countries = ['afganistan', 'albania', 'algeria']
index_albania = countries.index('albania') # = 1
pop[index_albania] # = 2.77

#Using dictionaries

Convert the data into a dictionary
pop = { "afganistan": 30.55, "albania":2.77, "algeria"39.21}
pop["albania"] # to call the key

world['sealand'] = 'sealand' # initialize a dictionary with a unique value
#check if a value is in a dictionary
"sealand" in world # returns a boolean
world['sealand'] = 0.000028
print('sealand' in world)
del(world['sealand'])

# Creating a DataFrame using a dictionary (where the data is initialized in lists)

import pandas as pd

my_dict = {'country' :names,
            'drives_right':dr,
            'cars_per_cap':cpc
            }

cars = pd.DataFrame(my_dict)