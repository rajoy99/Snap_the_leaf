import connection
curr=connection.cursor();
def validuser(email,password):
    sqlcmd="select email ,password from usertable where email=%s and password=%s" % (email,password);
    curr.execute(sqlcmd);
    result=curr.fetchall();
    if(result.exists):
        return True;
    else:
        return False;

    