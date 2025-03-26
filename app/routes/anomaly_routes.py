from flask import Blueprint, request, jsonify
from app.models.anomaly_model import extract_features
from sklearn.metrics.pairwise import cosine_similarity
import os

bp = Blueprint('anomaly', __name__)

@bp.route('/upload', methods=['POST'])
def upload_images():
    try:
        if 'image1' not in request.files or 'image2' not in request.files:
            return jsonify({'error': 'No images provided'}), 400

        image1 = request.files['image1']
        image2 = request.files['image2']

        # Save images temporarily
        image1_path = "image1.jpg"
        image2_path = "image2.jpg"
        image1.save(image1_path)
        image2.save(image2_path)

        # Extract features for both images
        features1 = extract_features(image1_path)
        features2 = extract_features(image2_path)

        if features1 is None or features2 is None:
            return jsonify({'error': 'Error extracting features from one or both images'}), 500

        # Calculate cosine similarity between the two feature vectors
        similarity = cosine_similarity([features1], [features2])[0][0]

        # Clean up the saved images
        os.remove(image1_path)
        os.remove(image2_path)

        return jsonify({'similarity_score': float(similarity)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500 