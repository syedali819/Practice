
import numpy as np
import pandas as pd

example_dictionary = {
    "col1":[10000,2,"Ali",40,5,6],
    "col2":[20000,3,"Ali",50,5,6],
    "col3":[30000,4,"Ali",60,5,6]
    }
# Convert dictionary to DataFrame
df = pd.DataFrame(example_dictionary)

# Display the DataFrame
print(df.head(5))

# Access the element 30000
value = df.loc[:,["col1","col2","col3"]]
print("\n The value is: \n ", value)

df = pd.read_csv('First.csv', delimiter=',')

print(df.head(5))
