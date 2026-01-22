import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('r"C:\Users\STUDENT\Downloads\archive (6)\marketing_campaign.csv")
print(df.columns)
print(df.info())
print(df.isnull().sum())
 
df['Age']=2026 - df['Year_Birth']
plt.figure(figsize=(10,5))
sns.boxplot(x=df['Age'],color='lightblue')

plt.title("Age Distribution")
plt.show()
plt.figure(figsize=(10,5))
plt.show()
