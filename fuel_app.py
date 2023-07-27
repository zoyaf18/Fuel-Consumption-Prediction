from flask import Flask, request, render_template
import joblib
app = Flask(__name__)
model = joblib.load("model.save")

app = Flask(__name__, template_folder='templates')

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    X_test = [[float(x) for x in request.form.values()]]
    print('actual',X_test)
    pred = model.predict(X_test)
    
    return render_template('Manual_predict.html', \
                Prediction_Output = ('Car Fuel Consumption(L/100km): ', pred[0]))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    