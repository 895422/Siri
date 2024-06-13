from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    backend_response = requests.get('http://backend-service:5000').json()
    return render_template('index.html', message=backend_response['message'])

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('data')
    requests.post('http://backend-service:5000/data', json={"data": data})
    return 'Data submitted successfully'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
