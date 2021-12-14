import os


class Config:
    """
    This class represent database configuration
    """
    __username = os.getenv('DB_USER', 'sqlalchemy')
    __password = os.getenv('DB_PASS', 'sqlalchemy')
    __host = os.getenv('DB_HOST', 'localhost')
    __port = os.getenv('DB_PORT', '5432')
    __db_name = os.getenv('DB_NAME', 'InstaCook')

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{__username}:{__password}@{__host}:{__port}/{__db_name}'  # Tells where DB present
    SQLALCHEMY_TRACK_MODIFICATIONS = False
