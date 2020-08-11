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
    no_data_counter = 0
    indices = []
    for i in df[column_name].index:
        if str(type(df[column_name][i])) == "<class 'str'>":
            if df[column_name][i].strip() == no_data:
                indices.append(i)
                no_data_counter += 1
        else:
            if df[column_name][i] == no_data:
                indices.append(i)
                no_data_counter += 1

    df.drop(indices, axis = 0, inplace = True)
    
    if no_data_counter != 0:
        print("\n{} rows with no data in column '{}' was removed successfully!\n".format(no_data_counter, column_name))
    else:
        print("\nno rows with no data in column '{}' was found!\n".format(column_name))

        
def col_to_int(df, column_name):
    """
    transforms all data in a specific column to integers.
    This is needed because sometimes data entry mistakes cause conflict in data types in columns.

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
    for idx in df[column_name].index:
        element = df[column_name][idx]
        
        if str(type(element)) == "<class 'int'>":
            int_counter += 1

        elif str(type(element)) == "<class 'float'>":
            float_counter += 1
            df[column_name][idx] = int(element)


        elif str(type(element)) == "<class 'str'>":
            str_countr += 1

            # check for commas
            x = ""
            for i in range(len(element.split(','))):
                x += element.split(',')[i]
                
            df[column_name][idx] = int(x.split('.')[0])                
            
        else:
            unknown_types.append(str(type(element)))
            
        counter += 1

    unknown_types = pd.Series(data = unknown_types)

    # make sure no elemets are missing
    if int_counter + float_counter + str_countr == counter:
        print("\nall elements in column '{}' are successfully transformed into integers\n".format(column_name))

    else:
        if unknown_types.unique()[0] == "<class 'numpy.float64'>":
            print("\nall elements in column '{}' are successfully transformed into floats\n".format(column_name))
        else:
            print("\n{} elements in column '{}' are missing with types:\n{}".format((counter - (int_counter + float_counter + str_countr)), column_name, unknown_types.unique()))


def col_to_float(df, column_name):
    """
    transforms all data in a specific column to floats.
    This is needed because sometimes data entry mistakes cause conflict in data types in columns.

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
    for idx in df[column_name].index:
        element = df[column_name][idx]
        
        if str(type(element)) == "<class 'float'>":
            float_counter += 1
            

        elif str(type(element)) == "<class 'int'>":
            int_counter += 1
            df[column_name][idx] = float(element)

        elif str(type(element)) == "<class 'str'>":
            str_countr += 1
            
            # check for commas
            x = ""
            for i in range(len(element.split(','))):
                x += element.split(',')[i]
                
            df[column_name][idx] = float(x)
            
        else:
            unknown_types.append(str(type(element)))
            
        counter += 1

    unknown_types = pd.Series(data = unknown_types)

    # make sure no elemets are missing
    if float_counter + int_counter + str_countr == counter:
        print("\nall elements in column '{}' are successfully transformed into floats\n".format(column_name))
        
    else:
        if unknown_types.unique()[0] == "<class 'numpy.float64'>":
            print("\nall elements in column '{}' are successfully transformed into floats\n".format(column_name))
        else:
            print("\n{} elements in column '{}' are missing with types:\n{}".format((counter - (int_counter + float_counter + str_countr)), column_name, unknown_types.unique()))


def str_col_process(df, column_name, separator = " ", case_sensitive = False):
    """
    processes data in string columns and prepares them for grouping by unifying all unique values.
    This is needed because sometimes data entry mistakes causes repeated unique values.

    Example:
        assume we have a column of country names, a data entry mistake might be writing
        country names in different way such as 'Egypt' and 'egypt'. This gives wrong results
        if we try grouping data by country without handling this issue first.

    Usage Example:
        - if input string is "Faculty of Engineering  " with separator = '_' and case_sensitive = False
        >> the output will be "faculty_of_engineering"

    Paramaters:
        - df: pandas dataframe
        - column_name: columne index on which the processing will be done
        - separator: if the string has multiple words, separate them with this parameter
        - case_sensitive: if True, data is left as is, otherwise, data is set to lower case for standarda
        
    Returns:
        - None: nothing is returned, the passed df is processed in place
    """
    # make sure all data are strings
    to_str(df = df, column_name = column_name)
    
    counter = 0

    for i in df[column_name].index:

        element = df[column_name][i].strip()

        new_element = ""
        
        # check for special characters and replace them with the separator
        check = 0
        for x in element:
            # check for special characters
            if not x.isalnum():
                check += 1
                # check if it's the first character, if yes, don't place a serarator 
                if x != element[0]:
                    # chaeck if it's the last character, if yes, don't place a serarator
                    if x != element[-1]:
                        # check if the previous character is a special character, if yes, don't place a serarator 
                        if check == 1:
                            new_element += separator
                        else:
                            pass
                    else:
                        pass 
                else:
                    pass
                        
            else:
                check = 0
                new_element += x
            
        # if data is not case sensitive, make all data in lower case
        if not case_sensitive:
            df[column_name][i] = new_element.strip().lower()
        else:
            df[column_name][i] = new_element.strip()
            
        counter += 1
        
    print("\nall elements in column '{}' are successfully processed and transformed into strings\n".format(column_name))

def to_str(df, column_name):
    """
    transforms all data in a specific column to Strings.
    This is needed because sometimes data entry mistakes cause conflict in data types in columns.

    Paramaters:
        - df: pandas dataframe
        - column_name: columne index on which the processing will be done
        
    Returns:
        - None: nothing is returned, the passed df is processed in place
    """
    counter = 0
    for element in df[column_name]:
        df[column_name].iloc[counter] = str(element)
        counter += 1

