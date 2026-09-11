import os
from dotenv import load_dotenv
import psycopg2
import numpy as np

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()
cursor.execute("SELECT age FROM customers WHERE age IS NOT NULL LIMIT 1000;")
age = cursor.fetchall()

customer_age = np.array(age).flatten()

print("Max Age:", customer_age.max())

print("Min Age:", customer_age.min())

print("Meam Age:", customer_age.mean())
