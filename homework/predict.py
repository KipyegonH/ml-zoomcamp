import pickle
from flask import Flask, request, jsonify

model_file = "model1.bin"
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)    

app = Flask("score")

@app.route('/score', methods=['POST'])
def predict():
    client =request.get_json()

    x= dv.transform([client])
    y_pred= model.predict_proba(x)[0,1]
    score=y_pred >=0.5

    result = {
        'score_probability': float (y_pred),
        'score': bool(score)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)

