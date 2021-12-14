import connection,requests,checkvalidtion,usefulhasing
from flask.templating import render_template_string

mycursor=connection.cursor();




def registration(email,password):
     em=email;
     pw=password;
     if not checkvalidtion.is_correct_email_formot(em):
        
        raise Exception("format of email is not excepted")
        
     if not (checkvalidtion.is_minimum_length(pw)):
          
          raise Exception("password length is not at minimum")
    

  
    
def start_with_hash_password(em,pw,foldername):
     
     try:
      sqlcmd="INSERT INTO usertable (email,password,foldername) VALUES (%s,%s,%s)"
      
      
      pw=usefulhasing.p_hash(pw)
      variable=(em,pw,foldername)
      
       
      mycursor.execute(sqlcmd,variable)
      connection.mydb.commit()
      return True
     
     except(RuntimeError):
     
      print("Sorry for inappropiate action ")
     
      return False
     finally:
      print("The 'try except' is finished")  
    

      

def is_real_add(em):
    res=requests.get("https://isitarealemail.com/api/email/validate",
    params = {'email': em})
    status=res.json()['status']
    if status == 'valid':
        return True
    else :
        return False;






