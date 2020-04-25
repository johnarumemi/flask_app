# defining these classes should enable us to change configurations
# from Development to Production easily

class Config(object):
    pass

class ProdConfig(Config):
    # Inherits from the first class
    pass

class DevConfig(Config):
    DEBUG = True
    # below is needed by sqlalchemy to connect to database
    # postgressql+psycopg2://user:password@ip:port/db_name
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:johnarumemi@localhost:5432/learning"

    # The below will print out the SQL queries being sent to the database
    SQLALCHEMY_ECHO = True
