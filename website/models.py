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
    def get_data(cls):
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("SELECT * FROM colleges")
            colleges = cursor.fetchall()
            return colleges
        except Exception as e:
            print(f"Error fetching college data: {str(e)}")
            return None
        finally:
            cursor.close()