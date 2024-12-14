from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('mysql+pymysql://root:410272085@localhost:3306/service')

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")
