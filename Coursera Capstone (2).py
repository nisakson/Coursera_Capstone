#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Import libraries
import pandas as pd
import numpy as np
import urllib.request
from bs4 import BeautifulSoup

# Specify the url
url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

# Open the url
page = urllib.request.urlopen(url)

# Parse the HTML from the URL into the parse tree format
soup = BeautifulSoup(page, "lxml")

# Find the right table
all_tables=soup.find_all("table")
right_table=soup.find('table', class_='wikitable sortable')

# Sort rows
A=[]
B=[]
C=[]

# Read each row of the table
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==3:
        # Check if the borough is not assigned
        if cells[1].find(text=True)!="Not assigned\n":
            # Find the name of the postal code to add to the cell
            addas = cells[0].find(text=True)
            # Remove the \n at the end of each term
            adda = addas[0:-1]
            # Repeat for borough
            addbs = cells[1].find(text=True)
            addb = addbs[0:-1]
            # Check if the neighborhood is not assigned
            if cells[2].find(text=True)=="Not assigned\n":
                # If the neighborhood is not assigned, assign it to the burrow value
                addc = addb
            else:
                # If the neighborhood is assigned find its name just as the postal code and neighborhood were done
                addcs = cells[2].find(text=True)
                addc = addcs[0:-1]
                # Check if the postal code has already been added to the table
                if adda in A:
                    # If it has, append the borough and neighborhood to the row
                    index = np.where(A == adda)
                    B[index].append(", ",addb)
                    C[index].append(", ",addc)
                else: 
                    # If it has not, create a new row with the postal code, borough, and neighborhood
                    A.append(adda)
                    B.append(addb)
                    C.append(addc)

# Put into a dataframe and display
df=pd.DataFrame(A,columns=['PostalCode'])
df['Borough']=B
df['Neighborhood']=C
df


# In[26]:


# Print the shape 
df.shape


# In[86]:


# Import file into a dataframe
import requests
url = "http://cocl.us/Geospatial_data"
df2 = pd.read_csv(url)

# Instantiate latitude and longitude columns for df
lat=[]
long=[]

# Iterate through each postal code
for row in df['PostalCode']:
    # Find the row which contains the postal code in df2
    index = df2[df2['Postal Code']==row].index.values
    indexes = index[0]
    # Find the associated latitude and longitude
    addlat = df2.iloc[indexes,1]
    addlong = df2.iloc[indexes,2]
    # Add the latitude and longitude to an array
    lat.append(addlat)
    long.append(addlong)
            
# Put into a dataframe, add latitude and longitude columns, and display
dfnew=df
dfnew['Latitude']=lat
dfnew['Longitude']=long
dfnew


# In[ ]:





# In[ ]:




