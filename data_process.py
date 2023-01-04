import pandas as pd
import os

files = list(filter(lambda file: 'xlsx' in file, os.listdir()))

for i, j in enumerate(files):
	print(i,' ',j )

file_name = input('enter the file name:  ')

df = pd.read_excel(file_name)

column_names = df.columns

num_of_columns = len(column_names)

for i in range(1, num_of_columns):
	df_new = df[[column_names[0],column_names[i]]].dropna()
	filename = column_names[i] + '.xlsx'
	df_new.to_excel(filename, index=False)
	print(f'{filename} is done. Completed {num_of_columns-1} datasets')
	
print(f'Completed {num_of_columns-1} datasets')



