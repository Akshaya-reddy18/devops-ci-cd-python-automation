import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home endpoint accessed")
    return jsonify({
        "status": "success",
        "message": "Welcome to the Python DevOps CI/CD Demo API!",
        "version": "1.0.0",
        "environment": os.environ.get("FLASK_ENV", "development")
    })

@app.route('/health')
def health_check():
    app.logger.info("Health check endpoint accessed")
    return jsonify({
        "status": "healthy",
        "service": "api"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
