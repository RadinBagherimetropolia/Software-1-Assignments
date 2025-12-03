
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/prime_number/<number>')
def calculate(number):
    try:
        num = int(number)
    except ValueError:
        response = {"message": "Invalid number", "status": 400}
        json_response = json.dumps(response)
        return Response(response=json_response, status=400, mimetype="application/json")


    if num < 2:
        isPrime = False
    else:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break

    result = {
        "Number": num,
        "isPrime": isPrime
    }

    json_response = json.dumps(result)
    return Response(response=json_response, status=200, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(error_code):
    response = {"message": "Invalid endpoint", "status": 404}
    json_response = json.dumps(response)
    return Response(response=json_response, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


