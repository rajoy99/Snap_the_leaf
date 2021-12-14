import connection
con=connection.cursor()
def requestgiven(filepath,folder,uniqueidentity):
  sql="INSERT INTO userrequestforverdict (filepath,folder,uniqueidentity) VALUES (%s,%s,%s)"
  values=(filepath,folder,uniqueidentity)
  con.execute(sql,values)
  connection.mydb.commit()