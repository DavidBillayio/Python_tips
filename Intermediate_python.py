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

# slicing columns
print(cars.loc[:,['cars_per_cap', 'drives_right']])

And and Or for use on arrays
- np,logical_and()
- np.logical_or()
- np.logical_not()

#if statements
if condition :
    expression

#elif statements
if condition :
    expression
elif condition :
    expression
else:
    expression

# filtering pandas DataFrames

rows_needed = list["column"] > 10
or
DataFrame[DataFrame["column"] > 10]

#for multiple conditions
DataFrame[np.logical_and(DataFrame['column'] > 8, DataFrame['column'] <10)]

#while loop

while condition :
    expression

# for loop

for var in seq :
    condition

#enumerate function
 for index, x in enumerate(list) :
     print( "index" + str(index) ":" + str(x))
     #you can reference individual objects in a list using x['y']


#looping data structures
#dictionary
for key, value in dict.items() #this is a method
    expression

# n dimensional numpy array (prints out all values)
for val in np.nditer(array) #this is a function
    expression

# pandas dataframes

for label , row in DataFrame.iterrows() :
    print(label)
    print(row)
    print(row['column'])

#adding columns efficiently
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper() # locates the label in the new column "COUNTRY" and sets it to a new value.

cars["COUNTRY"]=cars['country'].apply(str.upper)

#random numbers
 np.random.rand()

#Random Walk

random_walk = [0]

# Complete the for loop
for x in range(100) :
    step = random_walk[-1]

    dice = np.random.randint(1,7)

    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

plt.plot()
plt.hist()
plt.scatter()
plt.show()



