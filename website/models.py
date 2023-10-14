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
        
    def get_data():
        if not mysql.connection.is_connected():
            print("Database connection is not established")
            return "Database connection is not established"
        else:
            print ("success")
            return "success"