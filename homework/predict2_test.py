import pickle
from flask import Flask, request, jsonify

model_file = r"C:\Users\hillarik\Desktop\MLzoomcamp\homework\model1.bin"
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

dv_file = r"C:\Users\hillarik\Desktop\MLzoomcamp\homework\dv.bin"
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in) 

client = {"job": "management", "duration": 400, "poutcome": "success"}
x= dv.transform([client])
y_pred= model.predict_proba(x)[0,1]
subscription = y_pred >=0.5
print('subscription probability:' ,y_pred)

if subscription ==True:
    print('client has subcribed to deposit')
else:
    print('client has not subscribed to deposit')