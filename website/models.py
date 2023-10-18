from website import mysql

class Colleges(object):
    def __init__(self, collegeCode=None, collegeName=None):
        self.collegeCode = collegeCode
        self.collegeName = collegeName
        
    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO colleges(collegeCode, collegeName) \
                VALUES('{self.collegeCode}', '{self.collegeName}')"
            
        cursor.execute(sql)
        mysql.connection.commit()
    
    def edit(self, originalCode):
        cursor = mysql.connection.cursor()
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