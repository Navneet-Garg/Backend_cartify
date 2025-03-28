from flask import Flask
from flask_cors import CORS
from app.routes import (
    anomaly_routes,
    chatbot_routes,
    login_routes,
    recommendation_routes,
    search_routes,
    sentiment_routes
)
from app.utils.db import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Initialize database
    init_db(app)

    # Register blueprints with original endpoints
    app.register_blueprint(anomaly_routes.bp)
    app.register_blueprint(chatbot_routes.bp)
    app.register_blueprint(login_routes.bp)
    app.register_blueprint(recommendation_routes.bp)
    app.register_blueprint(search_routes.bp)
    app.register_blueprint(sentiment_routes.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000) 