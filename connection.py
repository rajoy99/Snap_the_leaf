
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",
user="root",
password="kalam01711",
port="1711",
database="leaf"
)
def cursor():

    return mydb.cursor()


    
