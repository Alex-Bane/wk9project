from flask import Flask, render_template, request
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from models import character

password = getenv('MYSQL_ROOT_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:' + password + '@database:3306/database'
db = SQLAlchemy(app)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    char_class = requests.get("http://service2:5001/char_class")
    race = requests.get("http://service3:5002/race")
    stats = requests.post("http://service4:5003/stats", data=race.text)

    char = character(clss=str(char_class.text), race=str(race.text), stat=str(stats.text))
    db.session.add(char)
    db.session.commit()

    return render_template('index.html', char_class=char_class.text, race=race.text, stats=stats.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
