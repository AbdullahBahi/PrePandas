import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import pp

df = pd.read_excel("MusicData.xlsx")

counter=0
datalist=[]
for f in df['Format']:
    row=list(df.index[counter])
    row.append(f)
    datalist.append(row)
    counter+=1

Format = []
Metric = []
Year = []
Number_of_Records = []
Value_Actual = []

for i in datalist:
    Format.append(i[0])
    Metric.append(i[1])
    Year.append(i[2])
    Number_of_Records.append(i[3])
    Value_Actual.append(i[4])

newdf = pd.DataFrame({"Format":Format,
                      "Metric":Metric,
                      "Year":Year,
                      "Number of Records":Number_of_Records,
                      "Value (Actual)":Value_Actual
                    })

newdf.dropna(axis=0, inplace=True)

pp.drop_no_data(df = newdf, column_name="Value (Actual)", no_data="")

pp.col_to_float(df=newdf, column_name="Value (Actual)")

pp.str_col_process(df = newdf, column_name = "Format", separator = " ", case_sensitive = True)

grb = newdf.groupby(["Format"])["Value (Actual)"].count()

print(grb)




