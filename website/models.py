from website import mysql

class Colleges(object):
    def __init__(self, collegeCode=None, collegeName=None):
        self.collegeCode = collegeCode
        self.collegeName = collegeName
        
    def add(self):
        cursor = mysql.connection.cursor()
        if self.exists(None):
            return "duplicate"
        
        sql = f"INSERT INTO colleges(collegeCode, collegeName) \
                VALUES('{self.collegeCode}', '{self.collegeName}')"
        cursor.execute(sql)
        mysql.connection.commit()
    
    def edit(self, originalCode):
        cursor = mysql.connection.cursor()
        if self.exists(originalCode):
            return "duplicate"
        
        sql = f"UPDATE colleges SET collegeCode = '{self.collegeCode}', collegeName = '{self.collegeName}' WHERE collegeCode = '{originalCode}'"
        cursor.execute(sql)
        mysql.connection.commit()

        
    def delete(self):
        cursor = mysql.connection.cursor()
        sql = f"DELETE FROM colleges WHERE collegeCode = '{self.collegeCode}'"
        cursor.execute(sql)
        mysql.connection.commit()
          
    #@classmethod
    def list():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM colleges")
        full_list = cursor.fetchall()
        return full_list
    
    def exists(self, originalCode):
        cursor = mysql.connection.cursor()
        if originalCode:
            cursor.execute("SELECT 1 FROM colleges WHERE collegeCode = %s AND collegeCode != %s", (self.collegeCode, originalCode))
        else:
            cursor.execute("SELECT 1 FROM colleges WHERE collegeCode = %s", (self.collegeCode,))
        return cursor.fetchone() is not None

    @classmethod
    def search(cls, query):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM colleges WHERE collegeCode LIKE '%{query}%' OR collegeName LIKE '%{query}%'"
        cursor.execute(sql)
        search_results = cursor.fetchall()
        return search_results

class Students(object):
    def __init__(self, studentID=None, firstName=None, lastName=None, course=None, yearLevel=None, gender=None):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.course = course
        self.yearLevel = yearLevel
        self.gender = gender
        
    def list():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM students")
        full_list = cursor.fetchall()
        return full_list
    
class Courses(object):
    def __init__(self, courseCode=None, courseName=None, college=None):
        self.courseCode = courseCode
        self.courseName = courseName
        self.college = college
        
    def list():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM courses")
        full_list = cursor.fetchall()
        return full_list
    
    def add(self):
        cursor = mysql.connection.cursor()
        if self.exists(None):
            return "duplicate"

        sql = f"INSERT INTO courses(courseCode, courseName, college) \
                VALUES('{self.courseCode}', '{self.courseName}', '{self.college}')"
        cursor.execute(sql)
        mysql.connection.commit()
        
    def edit(self, trueCourse):
        cursor = mysql.connection.cursor()
        if self.exists(trueCourse):
            return "duplicate"
        
        sql = f"UPDATE courses SET courseCode = '{self.courseCode}', courseName = '{self.courseName}', college = '{self.college}' WHERE courseCode = '{trueCourse}'"
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def list_colleges(cls):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM colleges")
        colleges = cursor.fetchall()
        return colleges
    
    def exists(self, trueCourse):
        cursor = mysql.connection.cursor()
        if trueCourse:
            cursor.execute("SELECT 1 FROM courses WHERE courseCode = %s AND courseCode != %s", (self.courseCode, trueCourse))
        else:
            cursor.execute("SELECT 1 FROM courses WHERE courseCode = %s", (self.courseCode,))
        return cursor.fetchone() is not None
    