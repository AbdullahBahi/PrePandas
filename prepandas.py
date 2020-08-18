# PROGRAMMER: Abdullah Bahi
# DATE CREATED: 6/60/2020
# PURPOSE: This module contains functions for pre-processing structured data in pandas dataframes. 
#
# FUNCTIONS:
#       - drop_no_data(df, column_name, no_data = "")
#       - col_to_int(df, column_name)
#       - col_to_float(df, column_name)
#       - str_col_process(df, column_name, separator = " ", case_sensitive = False)
#       - to_str(df, column_name)
##       

import pandas as pd

def drop_no_data(df, column_name, no_data = ""):
    """
    if columns contain a special character or string to refer to lack of data, this
    function drops all rows with such charachters in the specified column.
    
    Paramaters:
        - df: pandas dataframe
        - column_name: columne index on which the processing will be done
        - no_data: special character used for no data in the dataset
        
    Returns:
        - None: nothing is returned, the passed df is processed in place
    """
    counter = 0
    for i in range(len(df[column_name])):
        if str(type(df[column_name].iloc[i])) == "<class 'str'>":
            if df[column_name].iloc[i].strip() == no_data:
                df.drop([i], axis = 0, inplace = True)
                counter += 1
        else:
            if df[column_name].iloc[i] == no_data:
                df.drop([i], axis = 0, inplace = True)
                counter += 1

    if counter != 0:
        print("\n{} rows with no data removed successfully!\n".format(counter))
    else:
        print("\nno rows with no data was found!\n")

        
def col_to_int(df, column_name):
    """
    transforms all column data to integers.

    Paramaters:
        - df: pandas dataframe
        - column_name: columne index on which the processing will be done

    Returns:
        - None: nothing is returned, the passed df is processed in place
    """
    
    counter = 0
    int_counter = 0
    float_counter = 0
    str_countr = 0
    unknown_types = []

    # iterate the column and check for data type, if not int, tranform to int.
    for element in df[column_name]:
        
        if str(type(element)) == "<class 'int'>":
            int_counter += 1

        elif str(type(element)) == "<class 'float'>":
            float_counter += 1
            df[column_name].iloc[counter] = int(element)


        elif str(type(element)) == "<class 'str'>":
            str_countr += 1

            # check for commas
            x = ""
            for i in range(len(element.split(','))):
                x += element.split(',')[i]
                
            df[column_name].iloc[counter] = int(x.split('.')[0])                
            
        else:
            unknown_types.append(str(type(element)))
            
        counter += 1

    unknown_types = pd.Series(data = unknown_types)

    # make sure no elemets are missing
    if int_counter + float_counter + str_countr == counter:
        print("\nall elements in column {} are successfully transformed into integers\n".format(column_name))
    else:
        print("\n{} elements are missing with types:\n{}".format((counter - (int_counter + float_counter + str_countr)), unknown_types.unique()))


def col_to_float(df, column_name):
    """
    transforms all column data to floats.

    Paramaters:
        - df: pandas dataframe
        - column_name: columne index on which the processing will be done
        
    Returns:
        - None: nothing is returned, the passed df is processed in place
    """
    
    counter = 0
    int_counter = 0
    float_counter = 0
    str_countr = 0
    unknown_types = []

    # iterate the column and check for data type, if not int, tranform to int.
    for element in df[column_name]:

        if str(type(element)) == "<class 'float'>":
            float_counter += 1
            

        elif str(type(element)) == "<class 'int'>":
            int_counter += 1
            df[column_name].iloc[counter] = float(element)

        elif str(type(element)) == "<class 'str'>":
            str_countr += 1
            
            # check for commas
            x = ""
            for i in range(len(element.split(','))):
                x += element.split(',')[i]
                
            df[column_name].iloc[counter] = float(x)
            
        else:
            unknown_types.append(str(type(element)))
            
        counter += 1

    unknown_types = pd.Series(data = unknown_types)

    # make sure no elemets are missing
    if float_counter + int_counter + str_countr == counter:
        print("all elements in column '{}' are successfully transformed into floats\n".format(column_name))
        
    else:
        print("\n{} elements are missing with types:\n{}".format((counter - (int_counter + float_counter + str_countr)), unknown_types.unique()))


def str_col_process(df, column_name, separator = " ", case_sensitive = False):

    # make sure all data are strings
    to_str(df = df, column_name = column_name)
    
    counter = 0

    for element in df[column_name]:

        # check for special characters and replace them with the separator
        char_counter = 0
        for x in element:
            if not x.isalnum():
                element[char_counter] = separator
            else:
                pass
        # if data is not case sensitive, make all data in lower case
        if not case_sensitive:
            df[column_name].iloc[counter] = element.strip().lower()
        else:
            df[column_name].iloc[counter] = element.strip()
            
        counter += 1

def to_str(df, column_name):
    counter = 0
    for element in df[column_name]:
        df[column_name].iloc[counter] = str(element)
        counter += 1











