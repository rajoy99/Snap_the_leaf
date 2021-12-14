import connection
con=connection.cursor()
def diseaseforconformation():
    sql="SELECT filepath, userrequestforverdict.uniqueidentity, userrequestforverdict.folder FROM userrequestforverdict INNER JOIN verdictdetails ON userrequestforverdict.uniqueidentity =verdictdetails.uniqueidentity WHERE verdict='r'"
    
    con.execute(sql)
    result=con.fetchall()
    return result
