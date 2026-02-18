from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated Database
events = [
    {"id": 1, "name": "Astro Quiz", "dept": "AstroClub"},
    {"id": 2, "name": "Python Hackathon", "dept": "CSE"},
    {"id": 3, "name": "Stargazing", "dept": "AstroClub"}
]

@app.route('/')
def home():
    return "<h1>Eventopia ML Dashboard</h1>"

# Get all events
@app.route('/api/events')
def get_events():
    return jsonify(events)

# Filter events by department
@app.route('/api/events/<department>')
def filter_events(department):
    filtered = [e for e in events if e['dept'].lower() == department.lower()]
    return jsonify(filtered)

# Get event by ID
@app.route('/api/event/<int:event_id>')
def get_event(event_id):
    for event in events:
        if event["id"] == event_id:
            return jsonify(event)
    return jsonify({"error": "Event not found"}), 404

# Add a new event (POST)
@app.route('/api/events/add', methods=['POST'])
def add_event():
    data = request.get_json()

    new_event = {
        "id": len(events) + 1,
        "name": data["name"],
        "dept": data["dept"]
    }

    events.append(new_event)
    return jsonify(new_event), 201

if __name__ == '__main__':
    app.run(debug=True)
