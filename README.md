# PrePandas
Python library for pre-processing missy real-world pandas DataFrames

PrePandas is a library of helper functions to make data pre-processing while working with missy real-world pandas DataFrames much easier.

## Functions

### drop_no_data()
if columns contain a special character or string to refer to lack of data, this function drops all rows with such charachters in the specified column.

### col_to_int()
transforms all data in a specific column to integers. This is needed because sometimes data entry mistakes cause conflict in data types in columns.

### col_to_float()
transforms all data in a specific column to floats. This is needed because sometimes data entry mistakes cause conflict in data types in columns.

### to_str()
transforms all data in a specific column to Strings. This is needed because sometimes data entry mistakes cause conflict in data types in columns.

### str_col_process()
processes data in string columns and prepares them for grouping by unifying all unique values. This is needed because sometimes data entry mistakes causes repeated unique values.
**Example:**
assume we have a column of country names, a data entry mistake might be writing country names in different way such as 'Egypt' and 'egypt'. This gives wrong results if we try grouping data by country without handling this issue first.

## Usage Tips

1. load the data file into pandas DataFrame

2. create sub DataFrames for desired relationships (Extract desired columns) if required.  
   **NOTE**: it's a good practice to keep the original DataFrame with raw data and extract the desired data to other DataFrames for processing

3. drop or fill any row with NaN values in the sub DataFrames

4. pre-process the sub DataFrames using PrePandas library:
   - drop any row with no_data special string using drop_no_data function
   - transform and pre-process columns (int, float or string) to remove any data entry mistakes

5. now that data is pre-processed, do whatever operations and calculations you want on the data (mean, sum, normalizing, sorting, etc..)

6. visualize your calculations as desired (printing or plotting)

## Usage Example

The folder Music_Data contains an Excel data file of the format xlsx. This file contains information about different music genres and players, we pre-process the data using PrePandas library in order to prepare it for analysis as follows:  
```
import pandas as pd
import prepandas as pp

# load the data file into pandas DataFrame
df = pd.read_excel("MusicData.xlsx")

# drop or fill any row with NaN values in the sub DataFrames
df.dropna(axis=0, inplace=True)

# pre-process the sub DataFrames using PrePandas library
pp.drop_no_data(df = newdf, column_name="Value (Actual)", no_data="")
pp.col_to_float(df=newdf, column_name="Value (Actual)")
pp.str_col_process(df = newdf, column_name = "Format", separator = " ", case_sensitive = True)

# group different formats by by value counts
grb = newdf.groupby(["Format"])["Value (Actual)"].count()

# print the results
print(grb)
```
