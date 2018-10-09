#import packages
import pandas as pd
import numpy as np

#Read the original csv file
df_original=pd.read_csv("/home/mnallapa/DQFile.csv")

#Remove columns from the csv file and assign it to a new dataframe. We can also make changes to the original using inplace argument
df_position=df_original.drop(['Edition Statement','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Shelfmarks'],axis=1)

#Make a copy to demonstrate the difference between label vs position based indexing
df_index=df_position.copy()

#Set the Identifier as the index
df_position.set_index(['Identifier'],inplace=True)

#Show the difference between by getting row 206 both ways

#Check if the index is unique
df_position.index.is_unique

#Working with Date of publication
#Extract the first appearance of year and remove unwanted characters
df_position['Date of Publication']=df_position['Date of Publication'].str.extract(r'(\d{4})')

#Fill NaN values with zero and change datatype to integer
df_position['Date of Publication']=df_position['Date of Publication'].fillna(0).astype(int)

#Working with Place of publication
#Remove unwanted characters, remove spaces at the beginning and end, convert the data to lower case so that it will be easy to work with
df_position['Place of Publication']=df_position['Place of Publication'].str.replace('\W',' ').str.lower().str.strip()

#Get the list of top 10 frequent places. We will use this list to standardize most of the places
placelist=df_position['Place of Publication'].value_counts().head(10).index.tolist()

# Create boolean series for these frequent places
london=df_position['Place of Publication'].str.contains('london')
paris=df_position['Place of Publication'].str.contains('paris')
edinburgh=df_position['Place of Publication'].str.contains('edinburgh')
newyork=df_position['Place of Publication'].str.contains('new york')
leipzig=df_position['Place of Publication'].str.contains('leipzig')
philadelphia=df_position['Place of Publication'].str.contains('philadelphia')
berlin=df_position['Place of Publication'].str.contains('berlin')
boston=df_position['Place of Publication'].str.contains('boston')
dublin=df_position['Place of Publication'].str.contains('dublin')
oxford=df_position['Place of Publication'].str.contains('oxford')

# Use the boolean series to standardize the values for the frequent places, so that we will clean most of the places
df_position['Place of Publication']=np.where(london,'london',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(paris,'paris',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(edinburgh,'edinburgh',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(newyork,'New York',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(leipzig,'leipzig',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(philadelphia,'philadelphia',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(berlin,'berlin',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(boston,'boston',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(dublin,'dublin',df_test.str.replace('-',' '))
df_position['Place of Publication']=np.where(oxford,'oxford',df_test.str.replace('-',' '))


#Capitalize the places
df_position['Place of Publication']=df_position['Place of Publication'].str.capitalize()

#Write the clean dataframe to a csv file
df_position.to_csv("/home/mnallapa/DQ_Cleaned.csv")