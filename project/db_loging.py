import sys
import mariadb

def Connection_Database():
    try:
        connection = mariadb.connect(
            user = "root",
            password="testyan",
            host = "127.0.0.1",
            database = "projetm2"
        )
        connection.autocommit = False
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return connection


def user_exist(username):
    exist = False
    try:
        connection = Connection_Database()
        curs = connection.cursor()
        #param = tuple(username,)
        query = "SELECT count(id) FROM users WHERE username=?"
        curs.execute(query,(username,))
        #curs.execute("SELECT count(id) FROM users WHERE username='%s'".format(username))
        result = curs.fetchall()
        #print(result)
        for row in result:
            print(row[0])
            if row[0] == 1:
                exist = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    finally:
        #if connection.is_connected():
        curs.close()
        connection.close()
    return exist

def insert_user(username, password):
    try:

        connection = Connection_Database()
        curs = connection.cursor()
        curs.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
        #connection.commit()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    finally:
        #if connection.is_connected():
        curs.close()
        connection.close()

def check_password(username,password):
    check = False
    try:
        connection = Connection_Database()
        curs = connection.cursor()
        query = "SELECT Distinct password FROM users WHERE username=?"
        curs.execute(query,(username,))
        result = curs.fetchall()
        for row in result:
            if row[0] == password:
                check = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    finally:
        curs.close()
        connection.close()
    return check    

def get_data(database):
    result = None
    try:
        connection = Connection_Database()
        curs = connection.cursor()
        query = "SELECT * FROM {}".format(database)
        curs.execute(query)
        result = curs.fetchall()
        for row in result:
           print(row)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    finally:
        curs.close()
        connection.close()
    return result

def get_display_name(country):
    result = None
    database = "countries"
    display = ""
    try:
        connection = Connection_Database()
        curs = connection.cursor()
        query = "SELECT display_name,data_name FROM {} Where name=?".format(database)
        curs.execute(query,(country,))
        result = curs.fetchone()
       
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    finally:
        curs.close()
        connection.close()
    return result