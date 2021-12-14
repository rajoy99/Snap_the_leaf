import connection
con=connection.cursor()
def diseaseforconformation():
    sql="SELECT filepath, userrequestforverdict.uniqueidentity, userrequestforverdict.folder FROM userrequestforverdict INNER JOIN verdictdetails ON userrequestforverdict.uniqueidentity =verdictdetails.uniqueidentity WHERE verdict='r'"
    
    con.execute(sql)
    result=con.fetchall()
    return result
def detailforfarmer(folder):
    sql="SELECT filepath, userrequestforverdict.uniqueidentity, verdictdetails.details FROM userrequestforverdict INNER JOIN verdictdetails ON userrequestforverdict.uniqueidentity =verdictdetails.uniqueidentity WHERE verdict='c' and userrequestforverdict.folder=%s"
    value=(folder,)
    
    con.execute(sql,value)
    result=con.fetchall()
    return result
