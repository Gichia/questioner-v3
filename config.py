"""Configuration settings for the app"""
import os

class Config(object):
    """Main configuration"""
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
    """Configurations for development"""
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    """Configurations for test"""
    FLASK_ENV = "testing"
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv("TEST_DATABASE_URL")

app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}