#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data

# Download data files from cloud storage (replace with your URLs)
# curl -o data/embeddings.pkl https://your-storage-url/embeddings.pkl
# curl -o data/filenames.pkl https://your-storage-url/filenames.pkl
# curl -o data/recommend_data.csv https://your-storage-url/recommend_data.csv
# curl -o data/final_file.csv https://your-storage-url/final_file.csv

# Install dependencies
pip install -r requirements-vercel.txt

# Create necessary directories
mkdir -p app/models
mkdir -p app/routes
mkdir -p app/utils
mkdir -p app/config 