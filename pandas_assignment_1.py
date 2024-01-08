'''
question 1.

import pandas as pd

s1 = [4 , 8 , 15 , 16 , 23 , 42]

x = pd.Series(s1)
print(x)

question 2.


import pandas as pd

myvar = [4 , 8 , 15 , 16 , 23 , 42 , 89 , 6 , 0 , 7]

x = pd.Series(myvar)
print(x)

question 3.

import pandas
import pandas as pd

x = pandas.read_csv('FILES/fetch_file.csv')

print(x)

question 4.
Data frames are two dimensional like having row and coloum , it is helping to manuplate structured data effectively , in series we have itmes in list
i.e single dimesional

question 5.
common function used in dataframe pd.dataframe() pd.read_csv()df.head(n) , df.tail(n)

question 6.
series is mutable ,data frame is mutable , panel is depreciated


question 7.
import pandas as pd

names = pd.Series(['Alice' , 'Bob' , 'Charlie'])
ages = pd.Series([25 , 30 , 35])
cities = pd.Series(['New York' , 'San Francisco' , 'Los Angeles'])

data = {'Name' : names , 'Age' : ages , 'City' : cities}
df = pd.DataFrame(data)

print(df)


'''
