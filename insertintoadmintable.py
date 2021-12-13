import connection
con=connection.cursor()
def insertvalues(email,password):
    sqlcmd="INSERT INTO admintable (emailaddress,password) VALUES (%s,%s)"
    values=(email,password)
    con.execute(sqlcmd,values)
    connection.mydb.commit()
insertvalues("abdullahbinkalam@gamil.com","kalam01711")
insertvalues("kalam01711@gmail.com","kalam01711")