# pandas
import pandas as pd

file_path = './read_CSV_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('\n')

df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')
