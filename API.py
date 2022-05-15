from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import re

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/v1/replaceThe', methods=['POST'])
@cross_origin()
def replaceTHE():
    replacedText = request.json["initial-para"]

    # Replace the word "the" with "a"
    t1 = re.sub(r'\bthe\b', 'alpha', replacedText.lower())
    t2 = re.sub(r'\bthe\b', 'beta', replacedText.lower())
    t3 = re.sub(r'\bthe\b', 'gamma', replacedText.lower())
    t4 = re.sub(r'\bthe\b', 'theta', replacedText.lower())

    return jsonify({
            "alpha": t1,
            "beta": t2,
            "gamma": t3,
            "theta": t4
        })


if __name__ == "__main__":
    app.run(debug=True)