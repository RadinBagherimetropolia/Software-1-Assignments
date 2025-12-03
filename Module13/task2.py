import mariadb
from flask import Flask, Response
import json

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='RadinB1385',
    database='animals_game',
    autocommit=True
)

print("Connected to MariaDB successfully")

app = Flask(__name__)

@app.route('/airport/<icao>')
def airport_info(icao):
    sql = "SELECT name, iso_country FROM airport WHERE ident = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    results = cursor.fetchall()

    if len(results) == 0:
        response = {"message": "ICAO code not found", "status": 404}
        return Response(json.dumps(response), status=404, mimetype="application/json")

    name, location = results[0]
    response = {
        "ICAO": icao,
        "Name": name,
        "Location": location
    }

    return Response(json.dumps(response), status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)

