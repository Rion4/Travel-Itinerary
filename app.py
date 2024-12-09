from flask import Flask, request, jsonify

app = Flask(__name__)


itineraries = []

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/add', methods=['POST'])
def add_itinerary():
    data = request.get_json()
    destination = data['destination']
    start_date = data['start_date']
    end_date = data['end_date']
    activities = data['activities']

    new_itinerary = {
        'id': len(itineraries) + 1,
        'destination': destination,
        'start_date': start_date,
        'end_date': end_date,
        'activities': activities
    }
    itineraries.append(new_itinerary)

    return jsonify(new_itinerary), 201

if __name__ == '__main__':
    app.run(debug=True)
