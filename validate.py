import mysql.connector 


class Validate:
    def __init__(self, role, username, password, status, email=None):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='CBTapp',
            port=3306

        )
        self.cursor = self.db.cursor()
        self.username = username
        self.email = email 
        self.password = password
        self.status = status
        if role == 'login':
            self.login()
        elif role == 'signup':
            self.signup()

        if self.login() or self.signup():
            self.valid = True
        else:
            self.valid = False
        
    def __bool__(self):
        return self.valid
    def signup(self):
        myquery = ("INSERT INTO USERS (name, email, password) "
                    "VALUES(%s, %s, %s)")
        val = (self.username, self.email, self.password)

        try:
            self.cursor.execute(myquery, val)
            self.db.commit()
            return True

        except mysql.connector.Error as err:
            print(f'Error:{err} ')
            return False

    def login(self):
        query = "SELECT * FROM USERS WHERE name = %s AND password = %s"
        try:
            self.cursor.execute(query, (self.username, self.password))
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        
        except mysql.connector.Error as err:
            print(f'Error:{err} ')
            return False
        



