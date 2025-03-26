# E-commerce AI Services

A Flask-based REST API providing various AI-powered services for an e-commerce platform.

## Features

- User Authentication (Customer/Seller)
- AI Chatbot using Google's Gemini
- Image-based Product Recommendation System
- Anomaly Detection for Product Images
- Product Search by Type
- Sentiment Analysis for Reviews

## Prerequisites

- Python 3.8+
- MongoDB
- Google API Key (for chatbot)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/e-commerce-ai-services.git
cd e-commerce-ai-services
```

2. Create and activate a virtual environment:
```bash
python -m venv virtual_env
source virtual_env/bin/activate  # On Windows: virtual_env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your configuration:
```
GOOGLE_API_KEY=your_google_api_key
```

5. Place your data files in the `data/` directory:
- `embeddings.pkl`
- `filenames.pkl`
- `recommend_data.csv`
- `final_file.csv`

## API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /login` - Login user

### Chatbot
- `POST /chat` - Chat with AI assistant

### Recommendation System
- `POST /recommend` - Get product recommendations based on image

### Anomaly Detection
- `POST /upload` - Compare two images for anomalies

### Search
- `POST /get_data` - Search products by type

### Sentiment Analysis
- `POST /analyze` - Analyze sentiment of text

## Example Usage

### Register a new user
```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"id": "user@example.com", "password": "password123", "role": "customer"}'
```

### Get product recommendations
```bash
curl -X POST http://localhost:5000/recommend \
  -F "file=@product_image.jpg"
```

## Project Structure

```
FLASK/
├── app/
│   ├── models/         # AI models
│   ├── routes/         # API endpoints
│   ├── utils/          # Utility functions
│   └── config/         # Configuration
├── data/               # Data files
├── run.py             # Application entry point
└── requirements.txt   # Dependencies
```

## Deployment on Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy the application:
```bash
vercel
```

4. Set up environment variables in Vercel:
   - Go to your project settings in Vercel
   - Add the following environment variables:
     - `GOOGLE_API_KEY`
     - `MONGO_URI`
     - `FLASK_ENV=production`

5. For data files:
   - Upload your data files to a cloud storage service (e.g., AWS S3, Google Cloud Storage)
   - Update the file paths in `app/config/settings.py` to point to your cloud storage URLs

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini API for chatbot functionality
- PyTorch and ResNet50 for image processing
- MongoDB for data storage 