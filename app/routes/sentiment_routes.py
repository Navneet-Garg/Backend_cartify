from flask import Blueprint, request, jsonify
import json
from app.models.sentiment_model import generate_response

bp = Blueprint('sentiment', __name__)

@bp.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        raw_data = request.get_data(as_text=True)

        if not raw_data:
            return jsonify({"error": "Empty request body"}), 400

        # Manually parse JSON to avoid Content-Type issue
        try:
            data = json.loads(raw_data)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON format"}), 400

        if 'text' not in data:
            return jsonify({"error": "Invalid request, 'text' field is required"}), 400

        user_text = data['text']
        response_data = generate_response(user_text)
        return jsonify(response_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500 