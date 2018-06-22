
import pandas as pd
df=pd.read_csv("training_titanic.csv")
df['Child']=0
df['Child'][df['Age']<18]=1

c1=df[df['Child']==1]
s=c1["Survived"].value_counts(normalize=True)
print("child survived:",s[1]*100)

c2=df[df['Child']==0]
s1=c2["Survived"].value_counts(normalize=True)
print("old survived:",s1[1]*100)


#child=df['Survived'][df['Child']==1].value_counts()[1]
s