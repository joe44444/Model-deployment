#IMPORTS

from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pandas as pd
lr = joblib.load('model.pkl')
print("model loaded")
model_columns = joblib.load('model_columns.pkl')
print("model columns loaded")

#FLASK

app = Flask(__name__)
@app.route('/<ag>/<sx>/<emb>/', methods=['GET','POST'])

def predict(ag,sx,emb):
    a = []
    s = []
    e = []
    age = a.append(int(ag))
    sex = s.append(sx)
    embarked = e.append(emb)
    data = pd.DataFrame()
    data['Age'] = a
    data['Sex'] = s
    data['Embarked'] = e

    def preprocess(data):
        categoricals = []
        for col, col_type in data.dtypes.iteritems():
            if col_type == 'O':
                categoricals.append(col)
            else:
                data[col].fillna(0, inplace=True)
        df = pd.get_dummies(data, columns=categoricals, dummy_na=True)
        return df

    prep=preprocess(data)
    dt = prep.reindex(columns=model_columns, fill_value=0)
    prediction = lr.predict(dt)
    return jsonify('The answer is', str(prediction))


if __name__ == '__main__':
    app.run(host="localhost", port=7070, debug=True)




