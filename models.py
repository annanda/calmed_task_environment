from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TaskTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<id: {self.id}, task:{self.task}, timestamp:{self.timestamp}>'


class MoodTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(80), unique=False, nullable=False)
    task = db.Column(db.String(80), unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<id: {self.id}, mood:{self.mood}, task:{self.task}, timestamp:{self.timestamp}>'
