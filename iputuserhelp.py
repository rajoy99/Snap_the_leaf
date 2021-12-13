import connection
con=connection.cursor()
def insertvalues(folder,uniqueidentity,verdict):
    sqlcmd="INSERT INTO verdictdetails (folder,uniqueidentity,verdict) VALUES (%s,%s,%s)"
    values=(folder,uniqueidentity,verdict)
    con.execute(sqlcmd,values)
    connection.mydb.commit()