import pymysql 
import mysql_requestcount_property


if __name__ == '__main__':
    connection = pymysql.connect(host=mysql_requestcount_property.hostname, user=mysql_requestcount_property.user, password=mysql_requestcount_property.password, db=mysql_requestcount_property.database, charset=mysql_requestcount_property.charset)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("UPDATE APIKey SET currentReqCount = 0;")

    connection.commit()
    connection.close()
