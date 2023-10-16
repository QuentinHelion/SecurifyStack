"""
Main app file, all api route are declared there
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """
    Return pong
    """
    return jsonify({
        "result": "pong"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)