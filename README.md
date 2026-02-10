# Fraud Post Detection System for Social Media

A comprehensive machine learning-based fraud detection system that analyzes text, photos, and videos on social media platforms to identify fraudulent content.

**Scoring System:**  
Score > 50 = SAFE (Accept)  
30-50 = MONITOR (Admin review)  
< 30 = FRAUD (Block)

**Features include:**  
- Multi-Modal Analysis for text/photo/video  
- Advanced ML Models using DistilBERT and TensorFlow  
- Hybrid Detection with heuristics and ML  
- Persistent storage in SQLite/PostgreSQL with JSON backup  
- REST API

**Project includes files:**  
- `fraud_detection_system.py`  
- `fraud_detection_ml.py`  
- `api.py`  
- `client_example.py`  
- `config.py`  
- `requirements.txt`  
- `.env.example`

**Installation steps, API endpoints documentation, usage examples with cURL and Python, configuration details, scoring methodology, technologies used, security features, logging, testing, contributing guidelines, license (MIT), author (Nagendra Kusa - nagendrakusa87), support information, and additional resources.**