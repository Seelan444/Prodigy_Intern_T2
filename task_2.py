import pandas as pd 
import matplotlib.pyplot as plt
dataframe = pd.read_csv("gender_submission.csv")
print(dataframe.to_string())
print(dataframe.info())

# ====================== DATA CLEANING ========================

print(dataframe.isnull().sum())
print(f"Number of duplicate rows: {dataframe.duplicated().sum()}")
df = dataframe.drop_duplicates()
df['Survived'] = df['Survived'].astype(int)
print(df.head())

# ===================== EXPLORATORY DATA ANALYSIS ====================

print(df.describe())
print(df['Survived'].value_counts())
survival_rate = df['Survived'].mean()
print(f"Survival Rate: {survival_rate:.3%}")
print(dataframe.corr())

# ===================== RELATIONS WITH EACH OTHERS =========================

# bar plot
dataframe['Survived'].value_counts().plot(kind='bar', color=['red', 'yellow'])
plt.title('Survival Count of Passengers')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['Not Survived', 'Survived'], rotation=0)
plt.show()

# pie plot

dataframe['Survived'].value_counts().plot(kind='pie', labels=['Not Survived', 'Survived']
                                          , autopct='%1.1f%%', colors=['red', 'yellow'])
plt.title('Survival Distribution')
plt.ylabel('') 
plt.show()