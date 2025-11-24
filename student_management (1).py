students = {}   

def add_student(sid, name, cls):
    students[sid] = {"id": sid, "name": name, "class": cls, "subjects": {}}

def student_exists(sid):
    return sid in students

def get_student(sid):
    return students.get(sid)

def list_students():
    
    result = []
    for sid in students:
        student = students[sid]
        result.append((student["id"], student["name"], student["class"]))
    return result
