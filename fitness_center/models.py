from app import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class WorkoutSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    member = db.relationship('Member', back_populates='workout_sessions')

Member.workout_sessions = db.relationship('WorkoutSession', back_populates='member')
