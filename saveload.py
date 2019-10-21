#IMPORTS

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


#UPLOADS

df=pd.read_csv(r"C:\Users\Joe Rishwanth\Desktop\data\train.csv")
added=['Age','Embarked','Survived']
df1=df[added]


#PREPROCESSING DATA

categoricals = []
for col, col_type in df1.dtypes.iteritems():
    if col_type == 'O':
        categoricals.append(col)
    else:
        df1[col].fillna(30, inplace=True)
df2 = pd.get_dummies(df1, columns=categoricals, dummy_na=True)

#MODELLING

dependent_variable = 'Survived'
x = df2[df2.columns.difference([dependent_variable])]
y = df2['Survived']
lr = LogisticRegression()
lr.fit(x, y)


#SAVING MODEL

joblib.dump(lr,'model.pkl')
print("Model dumped!")


#LOADING MODEL

lr = joblib.load('model.pkl')


#saving the columns from train data

model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")








