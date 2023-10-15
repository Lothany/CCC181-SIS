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
        
    #@classmethod
    def get_data():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM colleges")
        colleges = cursor.fetchall()
        print("SQL acquired")
        return colleges