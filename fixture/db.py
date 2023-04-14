import pymysql


class DbFixture:

    def __init__(self, host, name, user, passsword):
        self.host = host
        self.name = name
        self.user = user
        self.password = passsword
        self.connection = pymysql.connect(host=host, database=name, user=user, password=passsword)

    def destroy(self):
        self.connection.close()
