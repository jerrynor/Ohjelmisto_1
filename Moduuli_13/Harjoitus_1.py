from flask import Flask, Response
import json

app = Flask(__name__)

def on_alkuluku(numero):

    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):

    result = {
        "Number": number,
        "isPrime": on_alkuluku(number)
    }

    json_data = json.dumps(result)

    return Response(json_data, mimetype='application/json')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
