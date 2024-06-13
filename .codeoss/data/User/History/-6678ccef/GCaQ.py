import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE_URL = (
    f"dbname='{os.getenv('DB_NAME')}' "
    f"user='{os.getenv('DB_USER')}' "
    f"password='{os.getenv('DB_PASSWORD')}' "
    f"host='{os.getenv('DB_HOST')}'"
)

conn = psycopg2.connect(DATABASE_URL)

@app.route('/')
def home():
    return jsonify({"message": "Hello from the backend!"})

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json.get('data')
    with conn.cursor() as cur:
        cur.execute("INSERT INTO mytable (data) VALUES (%s)", (data,))
        conn.commit()
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
