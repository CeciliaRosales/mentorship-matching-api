from flask import Flask, request, jsonify
from models import Mentee, Mentor
from matcher import match_all

app = Flask(__name__)
mentees = []
mentors = []

@app.route("/mentees", methods=["GET"])
def get_mentees():
    return jsonify([m.to_dict() for m in mentees])

@app.route("/mentees", methods=["POST"])
def add_mentee():
    data = request.get_json()
    mentee = Mentee(data["id"], data["name"], data["major"], data["subjects"], data["skills"], data["interests"])
    mentees.append(mentee)
    return jsonify(mentee.to_dict()), 201

@app.route("/mentors", methods=["GET"])
def get_mentors():
    return jsonify([m.to_dict() for m in mentors])

@app.route("/mentors", methods=["POST"])
def add_mentor():
    data = request.get_json()
    mentor = Mentor(data["id"], data["name"], data["major"], data["subjects"], data["skills"], data["interests"], data.get("capacity", 2))
    mentors.append(mentor)
    return jsonify(mentor.to_dict()), 201


@app.route("/matches", methods=["GET"])
def get_matches():
    return jsonify(match_all(mentees, mentors))

@app.route("/")
def index():
    return jsonify({
        "endpoints": ["GET /mentees", "POST /mentees", "GET /mentors", "POST /mentors", "GET /matches"]
    })

if __name__ == "__main__":
    app.run(debug=True)