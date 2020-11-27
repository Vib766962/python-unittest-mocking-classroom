import mysql.connector
class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="employees"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT MAX(salary) FROM salaries")
        myresult = mycursor.fetchall()
        #print(myresult)
        return myresult[0][0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        
    
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="employees"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT MIN(salary) FROM salaries")
        myresult = mycursor.fetchall()
        #print(myresult)
        return myresult[0][0]
        

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print("Max Salary is",max_salary)
    print("Min Salary is",min_salary)