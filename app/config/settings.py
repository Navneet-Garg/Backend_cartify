import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = "mongodb+srv://navneetg050:805020@firstmongo.izcl1mo.mongodb.net/testdb?retryWrites=true&w=majority"

# File paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Model paths
EMBEDDINGS_PATH = os.path.join(DATA_DIR, 'embeddings.pkl')
FILENAMES_PATH = os.path.join(DATA_DIR, 'filenames.pkl')
RECOMMEND_DATA_PATH = os.path.join(DATA_DIR, 'recommend_data.csv')
FINAL_FILE_PATH = os.path.join(DATA_DIR, 'final_file.csv')

# API Keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# CORS settings
ALLOWED_ORIGINS = ["http://localhost:3000"] 