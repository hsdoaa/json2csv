
#https://datatofish.com/json-string-to-csv-python/

import pandas as pd

df = pd.read_json (r'dblp_coauthorship.json')

authors = set(df[0]).union(set(df[1]))
authors_dict = {auth: i for i, auth in enumerate(authors, start=1)}

#print(authors_dict) 
print (df[0])
print("=========")
print(df[1])
df[0]=df[0].map(authors_dict)
df[1]=df[1].map(authors_dict)

#df.to_csv('co_authership.csv', index=False, header=['col1','col2','year'])

df1 = df.head(150000) #to filter the 1st 150000 rows of dataframe df which stores dblp_coauthorship.json

print("-------")
print(df1[df1.columns[2]]) #https://stackoverflow.com/questions/14941097/selecting-pandas-column-by-location
print("llllllll")

#filter by year for training

df_train=df1[( df1[df1.columns[2]]>=2000) & ( df1[df1.columns[2]]<=2010)]
df_train.drop(df_train.columns[2],axis=1,inplace=True)
df_train.to_csv('co_authership_training.csv', index=False, header=None)

#filter by year for testing

df_test=df1[( df1[df1.columns[2]]>=2011) & ( df1[df1.columns[2]]<=2015)]
df_test.drop(df_test.columns[2],axis=1,inplace=True)
df_test.to_csv('co_authership_testing.csv', index=False, header=None)

