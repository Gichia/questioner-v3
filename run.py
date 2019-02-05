''' Creates the base of the API'''
from config import app_config
from app import create_app

app = create_app("development")

if __name__ == "__main__":
    app.run()