from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import request, jsonify
from models import Member, db
from models import WorkoutSession

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "Member added successfully"}), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.query.get_or_404(id)
    return jsonify({"id": member.id, "name": member.name, "email": member.email})

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    member = Member.query.get_or_404(id)
    member.name = data['name']
    member.email = data['email']
    db.session.commit()
    return jsonify({"message": "Member updated successfully"})

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully"})

@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    new_workout = WorkoutSession(member_id=data['member_id'], date=data['date'], duration=data['duration'])
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({"message": "Workout session added successfully"}), 201

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.get_json()
    workout = WorkoutSession.query.get_or_404(id)
    workout.date = data['date']
    workout.duration = data['duration']
    db.session.commit()
    return jsonify({"message": "Workout session updated successfully"})

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    return jsonify({"id": workout.id, "member_id": workout.member_id, "date": workout.date, "duration": workout.duration})

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout session deleted successfully"})

@app.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_member_workouts(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    return jsonify([{"id": workout.id, "date": workout.date, "duration": workout.duration} for workout in workouts])

if __name__ == "__main__":
    app.run(debug=True)
