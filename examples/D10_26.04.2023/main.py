from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: str
    fullName: str
    mark: float
    className: str
    
student_data = [
    {
        "id": "2021001",
        "fullName": "Trần Văn Tèo",
        "mark": 9.9,
        "className": "21BITV01"
    },
    {
        "id": "2021002",
        "fullName": "Trần Thị Lý",
        "mark": 6.9,
        "className": "21BITV03"
    }
]

@app.get("/students", tags = ["students"])
def get_all_students():
    return student_data

@app.get("/students/{id}", tags = ["students"])
def get_student_by_id(id: str):
    sv = find_student_by_id(id)
    if sv:
        return {"success": True, "data": sv }
    else:
        return {"success": False, "message": f"Not found student id: {id}" }

@app.post("/students", tags = ["students"])
def create_new_student(student: Student):
    # Check student existed or not base on studentId
    sv = find_student_by_id(student.id)
    
    if sv:
        return {"success": False, 
                "message": f"student id: {student.id} is existed" }
    else:
        student_data.append(student)
        return {"success": True, "data": student_data }


def find_student_by_id(id):
    for sv in student_data:
        if sv["id"] == id:
            return sv
    return None
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def read_root(name):
    return {
        "message": f"Hello {name}. Have a nice day!"
    }
    
# chạy: $ uvicorn main:app --reload
# xem swagger: 127.0.0.1:8000/docs