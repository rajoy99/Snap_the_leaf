import connection
con=connection.cursor()
def updatedetails(uniqueidentity,verdict,details):
  sql="update verdictdetails set verdict = %s ,details = %s where uniqueidentity=%s"
  values=(verdict,details,uniqueidentity)
  con.execute(sql,values)
  connection.mydb.commit()


 