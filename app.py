from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS, cross_origin

from flask import request, flash

##sonuççç

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:karadeniz@34.121.66.9/IoT'
cors = CORS(app)

db = SQLAlchemy(app)


class info(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    email = db.Column(db.Integer)
    message = db.Column(db.Unicode)

    def __init__(self, name,  email, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.email = email
        self.message = message


@cross_origin()
@app.route('/contact2', methods=['POST'])
def contact_post():
    data = request.get_json(force=True)
    name = data["name"]
    email = data["email"]
    message = data["message"]

    new_user = info(name=name, email=email, message=message)

    db.session.add(new_user)
    db.session.commit()
    return "OK"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/contactMe', methods=['GET'])
def contactMe():
    return render_template("contactMe.html")
@app.route('/myClasses', methods=['GET'])
def classes():
    return render_template("myClasses.html")
@app.route('/movie', methods=['GET'])
def movies():
    return render_template("myFavoriteMovies.html")
@app.route('/book', methods=['GET'])
def books():
    return render_template("myFavoriteBooks.html")
@app.route('/webHomework', methods=['GET'])
def web():
    return render_template("weather.html")
@app.route('/myFriend', methods=['GET'])
def friend():
    return render_template("myFriend.html")
@app.route('/weather', methods=['GET'])
def weather():
    return render_template("weather.html")

if __name__ == '__main__':
    app.run()
