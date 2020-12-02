from flask import Flask, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/stats', methods=['GET','POST'])
def stats():
    stats = []
    while len(stats) < 6:
        stats.append(random.randint(3, 18))

    race = request.data.decode('utf-8')
    if race == "Human":
        bonus = "Bonus Stats: +1 to all"
        for stat in stats:
            list_number = 0
            stats[list_number] =  stats[list_number] + 1
            list_number += 1
    elif race == "Elf":
        bonus = "Bonus Stats: +2 to Dexterity, +1 to Wisdom"
        stats[1] = stats[1] + 2
        stats[4] = stats[4] + 1
    elif race == "Dwarf":
        bonus = "Bonus Stats: +2 to Constitution, +1 to Strength"
        stats[2] = stats[2] + 2
        stats[0] = Stats[0] + 1
    elif race == "Halfling":
        bonus = "Bonus Stats: +2 to Charisma, +1 to Dexterity"
        stats[5] = stats[5] + 2
        stats[1] = stats[1] + 1
    elif race == "Half-Orc":
        bonus = "Bonus Stats: +2 to Strength, +1 to Constitution"
        stats[0] = stats[0] + 2
        stats[2] = stats[2] + 1
    else:
        bonus = 'Race not found'
    #combined_string = bonus, "Strength:", stats[0], "Dexterity:", stats[1], "Constitution:", stats[2], "Intelgience:", stats[3], "Wisdom:", stats[4], "Charisma:", stats[5]
    return Response(bonus, mimetype="text/plain")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
