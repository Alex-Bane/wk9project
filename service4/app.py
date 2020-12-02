from flask import Flask, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/stats', methods=['GET','POST'])
def slogan():
    stats = []
    while len(stats) < 6:
        stats.append(random.randint(3, 18))

    race = request.data.decode('utf-8')
    if race == "Human":
        bonus = "Bonus Stats: +1 to all"
        for stat in len(stats):
            stats[stat] + 1

    elif race == "Elf":
        bonus = "Bonus Stats: +2 to Dexterity, +1 to Wisdom"
        stats[2] = stats[2] + 2
        stats[5] = stats[5] + 1
    elif race == "Dwarf":
        bonus = "Bonus Stats: +2 to Constitution, +1 to Strength"
        stats[3] = stats[3] + 2
        stats[1] = Stats[1] + 1
    elif race == "Halfling":
        bonus = "Bonus Stats: +2 to Charisma, +1 to Dexterity"
        stats[6] = stats[6] + 2
        stats[2] = stats[2] + 1
    elif race == "Half-Orc":
        bonus = "Bonus Stats: +2 to Strength, +1 to Constitution"
        stats[1] = stats[1] + 2
        stats[3] = stats[3] + 1
    else:
        bonus = 'Race not found'
    return Response(stats, bonus, mimetype="text/plain")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)