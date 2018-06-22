
import pandas as pd
df=pd.read_csv("training_titanic.csv")
#no of persons survived 
a=df["Survived"].value_counts()

a1=df["Survived"].value_counts(normalize=True)
print("survived",a1[1]*100)
print("dead",a1[0])

#no of male survived & died
d1=df[df["Sex"]=='male']
b=d1["Survived"].value_counts(normalize=True)
print("male survived:",b[1])
print("male dead:",b[0])

#no of female survived and died
d2=df[df["Sex"]=='female']
c=d2["Survived"].value_counts(normalize=True)
print("female survived:",c[1])
print("female dead:",c[0])