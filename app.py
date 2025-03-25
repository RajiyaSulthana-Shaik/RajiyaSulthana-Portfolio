from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/footer-title')
def footer_title():
    return jsonify({"name": "Shaik Rajiya Sulthana"})

if __name__ == '__main__':
    app.run(debug=True)
