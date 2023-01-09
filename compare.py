import pandas as pd
import csv
df1 = pd.read_csv('C:\\Users\\Dell\\Downloads\\bq-results-20221124-050220-1669266223525.csv')
df2 = pd.read_csv('C:\\Users\\Dell\\Downloads\\OMS_PO_LINES_202211241018.csv')

# result = df1[df1.apply(tuple,1).isin(df2.apply(tuple,1))]
# print(result)
#
# c_result_m = pd.merge(df1,df2)
# print(c_result_m)
with open('C:\\Users\\Dell\\Downloads\\bq-results-20221124-050220-1669266223525.csv', 'r') as csv1, open('C:\\Users\\Dell\\Downloads\\OMS_PO_LINES_202211241018.csv', 'r') as csv2:
    import1 = csv1.readlines()
    import2 = csv2.readlines()

with open('update.csv', 'w') as outFile:         # Create CSV file with differences
    for row in import1:
        if row not in import2:
            outFile.write(row)
