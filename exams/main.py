# Import libraries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Extracting the data we need to work with
df = pd.read_csv('data/exams.csv')
df = df.drop_duplicates()
print(df.head())


# The average of reading scores for students with/without the test preparation
prep = df.groupby('test preparation course')['reading score'].mean()
print(prep.head())

# The average of reading scores for students for different parental education levels
level = df.groupby('parental level of education')['reading score'].mean()
print(level.head())

race = df.groupby(['race/ethnicity', 'parental level of education', 'test preparation course'])[['reading score']].mean()
print(race)


# Creating plots for our findings
sns.catplot(x='test preparation course', y='reading score', data=df, kind='bar')
sns.catplot(x='parental level of education', y='reading score', data=df, kind='bar').set_xticklabels(rotation=35)
plt.show()
