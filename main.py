from flask import Flask,request,render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer


with open('model.pkl','rb')as file:
    loaded_model= pickle.load(file)

with open('vectorizer.pkl','rb')as file:
    vectorizer= pickle.load(file)





app= Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def home():
    prediction=None
    if request.method =='POST':
        input= request.form['text']
        input_vector= vectorizer.transform([input])
        prediction= loaded_model.predict(input_vector)[0].title()
        print (prediction)
    return render_template('index.html',prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)
