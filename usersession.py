from flask import session
def add_in_session(userid):
      session['userid']=userid
def logmeout():
      session.pop('userid',None);
def notLogOut():
    if 'userid' in session:
        return True;
    else:
        return False;

     