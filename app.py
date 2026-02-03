import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

itineraries = []

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/add', methods=['POST'])
def add_itinerary():
    try:
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
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)