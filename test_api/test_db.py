# 1connect to db
# 2. opened the scriptfile
# 3, write and execute 
# 4. read the tabel
import sqlite3

import pytest

# @pytest.mark.db
def sqlite():
    connection = sqlite3.connect("C:\\Users\\Nikitha\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db")
    cursor = connection.cursor()
    # cursor.execute("select a.AlbumId, a.Title ,a2.ArtistId ,a2.Name from Album a Inner Join Artist a2 on a.ArtistId = a2.ArtistId where a.ArtistId =2")
    cursor.execute("select * from Album")
    # data = cursor.fetchall()
    # print(cursor.rowcount())
    # print(len(data))
    # print(cursor.fetchone())
    # print(cursor.fetchmany(10))
    # print(cursor.description)
    # (('AlbumId', None, None, None, None, None, None), ('Title', None, None, None, None, None, None), ('ArtistId', None, None, None, None, None, None))
    colmns= cursor.description
    l1 = []
    for i in colmns:
       l1.append(i[0])
    data = cursor.fetchall()
    assert len(data)==347

    print(l1)

def sqlConnect(query):
    connection = sqlite3.connect("C:\\Users\\Nikitha\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.close()
    return cursor

# ============================================MYSQL
#pip install mysql-connector-python
# # @pytest.mark.db
# def test_sql():
#     connection = mysql.connector.connect(host="localhost",port=3306,database='mydb',user="tripur", password="123")
#     cursor = connection.cursor()
#     # cursor.execute("select a.AlbumId, a.Title ,a2.ArtistId ,a2.Name from Album a Inner Join Artist a2 on a.ArtistId = a2.ArtistId where a.ArtistId =2")
#     cursor.execute("select * from Album")
#     colmns= cursor.description
#     l1 = []
#     for i in colmns:
#        l1.append(i[0])
#     data = cursor.fetchall()
#     assert len(data)==347

#     print(l1)
# # ============================================POSTGreSql
# ##pip install psycopg2-binary
# def test_postGres():
#     connection = psycopg2.connect(host="localhost",port=3306,database='mydb',user="tripur", password="123")
#     cursor = connection.cursor()
#     # cursor.execute("select a.AlbumId, a.Title ,a2.ArtistId ,a2.Name from Album a Inner Join Artist a2 on a.ArtistId = a2.ArtistId where a.ArtistId =2")
#     cursor.execute("select * from Album")
#     colmns= cursor.description
#     l1 = []
#     for i in colmns:
#        l1.append(i[0])
#     data = cursor.fetchall()
#     assert len(data)==347

#     print(l1)

# # ============================================oracle

# ##pip install oracledb
# def oracle():
#     connection = oracledb.connect(host="localhost",port=3306,database='mydb',user="tripur", password="123")
#     cursor = connection.cursor()
#     # cursor.execute("select a.AlbumId, a.Title ,a2.ArtistId ,a2.Name from Album a Inner Join Artist a2 on a.ArtistId = a2.ArtistId where a.ArtistId =2")
#     cursor.execute("select * from Album")
#     colmns= cursor.description
#     l1 = []
#     for i in colmns:
#        l1.append(i[0])
#     data = cursor.fetchall()
#     assert len(data)==347

#     print(l1)

# # ============================================snwoflake

# ##pip install snowflake-connector-python
# def oracle():
#     connection = snowflake.connector.connect(host="localhost",port=3306,database='mydb',user="tripur", password="123", warehouse="wh",schema='sc')
#     cursor = connection.cursor()
#     # cursor.execute("select a.AlbumId, a.Title ,a2.ArtistId ,a2.Name from Album a Inner Join Artist a2 on a.ArtistId = a2.ArtistId where a.ArtistId =2")
#     cursor.execute("select * from Album")
#     colmns= cursor.description
#     l1 = []
#     for i in colmns:
#        l1.append(i[0])
#     data = cursor.fetchall()
#     assert len(data)==347

#     print(l1)