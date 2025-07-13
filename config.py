from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Configuration for the application
class Config:
    # Database configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_NAME = os.getenv('DB_NAME', 'mydatabase')
    DB_USER = os.getenv('DB_USER', 'myuser')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')

    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')

    # Other configurations can be added here

    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY', 'your-pinecone-api-key')
    PINECONE_INDEX = os.getenv('PINECONE_INDEX', 'your-pinecone-index')
    PINECONE_NAMESPACE = os.getenv('PINECONE_NAMESPACE', 'your-pinecone-namespace')
