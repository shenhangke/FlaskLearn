'''

@File    :   mysqlUtil.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-07-02 21:24   shenhangke      1.0         None
---------------------
 
'''

import MySQLdb


class mysql(object):
    def __init__(self):
        self.__hostname = "localhost"
        self.__user = "root"
        self.__passwd = "5166266skf"
        self.__db = "Flask"
        self.__port = 3306

    def getConnection(self):
        return MySQLdb.connect(host=self.__hostname, user=self.__user, passwd=self.__passwd
                               , db=self.__db, charset="utf8")

    def closeConnection(self, connection):
        if connection != None:
            connection.close()

    # 如果要避免sql注入攻击，要使用通过参数传值的方法。
    def testGetdata(self):
        try:
            connection = self.getConnection()
            try:
                cursor = connection.cursor()
                cursor.execute("select * from login where username=%s", ("shenhangke",))
                result = cursor.fetchall()
                for row in result:
                    # print("the row is :" + row)
                    print(row)
                    print(row[0] + " " + row[1])
            finally:
                self.closeConnection(connection)
        except Exception as e:
            print("the exception is" + e)

    def insertNameAndPasswd(self, username, passwd) -> bool:
        if (username != "") and (passwd != ""):
            try:
                connection = self.getConnection()
                try:
                    cursor = connection.cursor()
                    args = (username, passwd)
                    sql = "insert into login (username,passwd) values (%s,%s)"
                    cursor.execute(sql, args)
                    connection.commit()
                    return True
                except Exception as e:
                    connection.rollback()
                    print("execute error,the error is: "+e)
                    return False
                finally:
                    self.closeConnection(connection)
            except Exception as e:
                print("the exception is: " + e)
                return False

    def queryUserInfo(self,username,passwd):
        if username!="":
            try:
                connection=self.getConnection()
                try:
                    cursor=connection.cursor()
                    args=(username,passwd)
                    sql="select * from login where username=%s and passwd=%s"
                    cursor.execute(sql,args)
                    result=cursor.fetchall()
                    if len(result)!=0:
                        return True
                    else:
                        return False
                finally:
                    self.closeConnection(connection)
            except Exception as e:
                print(e)




if __name__ == "__main__":
    databaseUtil = mysql()
    print(databaseUtil.insertNameAndPasswd("qiuyinwei","123456"))
