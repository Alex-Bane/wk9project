from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/char_class', methods=['GET'])
def char_class():
    char_class = ["Fighter", "Rogue", "Wizard", "Ranger", "Cleric"]
    class_pick = char_class[random.randrange(0, 5)]

    return Response(random.choice(class_pick), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)