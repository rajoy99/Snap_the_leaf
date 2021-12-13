import connection
con=connection.cursor()
def isadmin(email,password):
    sql="select emailaddress,password from admintable where emailaddress = %s and password=%s"
    value=(email,password)
    con.execute(sql,value)
    result=con.fetchall()
    
    for user in result:
        if(user[0]==email):
         return True
        
    False
def adminlogin(email,password):
    sql="select emailaddress,password from admintable where emailaddress = %s and password = %s"

    value=(email,password)
    con.execute(sql,value)
    result=con.fetchall()
    print(result)
    for user in result:
        if(user[0]==email):
         return True
        
    False
def isuser(email,password):
     sql="select emailaddress,password from usertable  where emailaddress = %s and password = %s"
print(isadmin("abdullahbinkalam@gamil.com","kalam01711"))