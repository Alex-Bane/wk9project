from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/race', methods=['GET'])
def Race():
    race = ["Dwarf1", "Human1", "Elf1", "Half-Orc1", "Halfling1"]
    race_pick = race[random.randrange(0,5)]
    return Response(race_pick, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
