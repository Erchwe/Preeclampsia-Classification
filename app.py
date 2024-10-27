from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    features = np.array([[
        data.get('age'),
        data.get('gest_age'),
        data.get('height'),
        data.get('weight'),
        data.get('bmi'),
        data.get('sysbp'),
        data.get('diabp'),
        data.get('hb'),
        data.get('pcv'),
        data.get('tsh'),
        data.get('pp_13'),
        data.get('glycerides'),
        data.get('htn'),
        data.get('diabetes'),
        data.get('fam_htn'),
        data.get('diet'),
        data.get('sp_art'),
        data.get('activity'),
        data.get('sleep'),
        data.get('platelet'),
        data.get('creatinine'),
        data.get('plgf_sflt'),
        data.get('SEng'),
        data.get('cysC'),
        data.get('occupation')
    ]])

    prediction = model.predict(features)
    result = 'High Risk' if prediction[0] == 1 else 'Low Risk'
    return jsonify({'risk': result})

if __name__ == '__main__':
    app.run(debug=True)
