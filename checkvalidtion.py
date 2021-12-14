import connection
mycursor=connection.cursor()
import re
import usefulhasing
password =usefulhasing.p_hash("kalam01711")
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
def em_exit(em,pw):
    sqle="SELECT email, password FROM usertable WHERE email=%s and password=%s"
    mycursor.execute(sqle,(em,pw,))
    result=mycursor.fetchall()
    for values in result:
       if values[0]==em :
           return True
        
    return False
        
        
def is_correct_email_formot(email):
   
    if email_regex.match(email):
        return True
    else:
        return False
        
def is_minimum_length(password):
    if len(password)>=5:
     return True
    else:
     return False
def isregisteredemail(email):
    sqlcmd="select email  from usertable where email = %s" 
    var = (email,)
    mycursor.execute(sqlcmd,var)
    result=mycursor.fetchall()
    for user in result:
        if user[0]==email:
            return True
    return False

print(isregisteredemail("abdullahbinkhaleds@gmail.com"))
