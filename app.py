from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///default.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    release_date = db.Column(db.Date(), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Movie %r>' % self.title


@app.route('/')
def index():
    return 'flask-movies'


@app.route('/api/movies')
def api_movies():
    json = [movie.as_dict() for movie in Movie.query.all()]
    return jsonify(json)


if __name__ == '__main__':
    app.run()
