from flask import Flask, request, jsonify
from app import db
from app.models import BikePart

app = Flask(__name__)

# Route to search for bike parts by name
@app.route('/search_parts', methods=['GET'])
def search_parts():
    search_term = request.args.get('name')  # Get the search query from the URL
    if not search_term:
        return jsonify({"error": "No search term provided."}), 400

    # Query the database for bike parts that match the search term (case-insensitive)
    parts = BikePart.query.filter(BikePart.name.ilike(f"%{search_term}%")).all()

    if not parts:
        return jsonify({"message": f"No bike parts found for '{search_term}'."}), 404

    # Convert query results to a list of dictionaries
    parts_list = [{"name": part.name, "description": part.description, 
                   "where_to_buy": part.where_to_buy, "how_to_fix": part.how_to_fix} 
                  for part in parts]

    return jsonify(parts_list)

if __name__ == '__main__':
    app.run(debug=True)
