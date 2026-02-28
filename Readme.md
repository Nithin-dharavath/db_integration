📌 FastAPI + MySQL Integration (Single CREATE API):

A minimal backend project demonstrating integration of FastAPI with MySQL using SQLAlchemy ORM.
This project implements a single POST endpoint to create student records in a MySQL database.

🚀 Tech Stack:

🐍 Python 3.10+
⚡ FastAPI
🗄 MySQL
🔗 SQLAlchemy ORM
🔐 PyMySQL
📦 Pydantic

📂 Project Structure:

db_integration_tutorial/
│
├── main.py
├── requirements.txt
└── README.md

⚙️ Setup Instructions:

1️⃣ Clone Repository
git clone https://github.com/your-username/db_integration_tutorial.git
cd db_integration_tutorial

2️⃣ Create Virtual Environment:

python -m venv myenv
Activate : Windows - myenv\Scripts\activate

Mac/Linux - source myenv/bin/activate

3️⃣ Install Dependencies:

pip install -r requirements.txt
If requirements.txt not created:

pip install fastapi uvicorn sqlalchemy pymysql cryptography
🗄 MySQL Setup
Create Database
CREATE DATABASE college;
Create Table
USE college;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

🔐 Database Configuration:

In main.py, update:

from urllib.parse import quote_plus

db_password = quote_plus("your_mysql_password")

DATABASE_URL = f"mysql+pymysql://root:{db_password}@localhost:3306/college"

⚠ If your password contains special characters (@, #, %), quote_plus is required.

▶️ Run Application:

uvicorn main:app --reload

Server runs at: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

📌 API Endpoint

Create Student
POST /create
Request Body
{
  "name": "user name",
  "age": user age
}
Response
{
  "message": "Student created successfully",
  "data": {
    "id": 1,
    "name": "user name",
    "age": user age
  }
}