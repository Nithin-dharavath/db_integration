from fastapi import FastAPI, Depends
from urllib.parse import quote_plus
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# ==============================
# DATABASE CONFIGURATION
# ==============================
db_password = quote_plus("mysql-password-root")

DATABASE_URL = f"mysql+pymysql://root:{db_password}@localhost:3306/college"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ==============================
# TABLE MODEL
# ==============================

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

# ==============================
# Pydantic Schema
# ==============================

class StudentCreate(BaseModel):
    name: str
    age: int

# ==============================
# FastAPI App
# ==============================

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==============================
# CREATE API 
# ==============================

@app.get("/")
def home():
    return {"message" : "db_integration"}



@app.post("/create")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        age=student.age
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student created successfully",
        "data": {
            "id": new_student.id,
            "name": new_student.name,
            "age": new_student.age
        }
    }