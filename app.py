import numpy as np
from flask import Flask, request, jsonify,  render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('scm_reg', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')


@app.route('/predict', methods=['get','post'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    price = round(prediction[0], 2)
    return render_template('index1.html', prediction_text="The feight cost is $  {}".format(price))

if __name__=='__main__':
    app.run(debug=True)
