from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.tong', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', Total_timbulan_sampah=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    pengurangansampahtahunan, penanganansampahtahunan = [x for x in request.form.values()]

    data = []

    data.append(float(pengurangansampahtahunan,penanganansampahtahunan))
    
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', Total_timbulan_sampah=output, pengurangansampahtahunan=pengurangansampahtahunan, penanganansampahtahunan=penanganansampahtahunan)

if __name__ == '__main__':
    app.run(debug=True)