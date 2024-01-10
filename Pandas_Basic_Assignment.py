'''
Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

import pandas as pd

s1 = [4 , 8 , 15 , 16 , 23 , 42]

x = pd.Series(s1)
print(x)

Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
variable print it.


import pandas as pd

myvar = [4 , 8 , 15 , 16 , 23 , 42 , 89 , 6 , 0 , 7]

x = pd.Series(myvar)
print(x)

Q3. Create a Pandas DataFrame that contains the following data:

import pandas
import pandas as pd

x = pandas.read_csv('FILES/fetch_file.csv')

print(x)

Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.


Data frames are two dimensional like having row and coloum , it is helping to manuplate structured data effectively , in series we have itmes in list
i.e single dimesional

Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
you give an example of when you might use one of these functions?


common function used in dataframe pd.dataframe() pd.read_csv()df.head(n) , df.tail(n)

Q6. Which of the following is mutable in nature Series, DataFrame, Panel?


series is mutable ,data frame is mutable , panel is depreciated


Q7. Create a DataFrame using multiple Series. Explain with an example.


import pandas as pd

names = pd.Series(['Alice' , 'Bob' , 'Charlie'])
ages = pd.Series([25 , 30 , 35])
cities = pd.Series(['New York' , 'San Francisco' , 'Los Angeles'])

data = {'Name' : names , 'Age' : ages , 'City' : cities}
df = pd.DataFrame(data)

print(df)


'''
