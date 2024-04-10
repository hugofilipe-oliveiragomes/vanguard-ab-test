#!/usr/bin/env python
# coding: utf-8

# In[ ]:


datasets = {
    'Client Profiles': df1,
    'Digital Footprints': df34,
    'Experiment Roster': df2
}

for name, df in datasets.items():
    print(f"Dataset: {name}")
    print("Missing values:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())
    print("Dataframe info:")
    df.info()

