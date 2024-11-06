from phone_number_converter import PhoneNumberConverter
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
converter = PhoneNumberConverter()

# Load words when starting up
converter.load_words('dictionary.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    phone_number = request.json['phoneNumber']
    results = converter.convert_number(phone_number)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)