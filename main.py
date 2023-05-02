from turtle import Turtle,Screen
tur=Turtle()
screen=Screen()
tur.shape("circle")
screen.exitonclick()



































# import turtle as t
# my_t=t.Turtle()
# for i in range(20):
#     my_t.forward(10)
#     my_t.penup()
#     my_t.forward(10)
#     my_t.pendown()
#





# from turtle import Turtle,Screen
# my_tur=Turtle()
# print(my_tur)
# my_tur.shape("turtle")
# my_tur.color("coral")
# my_tur.forward(200)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("name",["selva","kumar"])
# table.align="r"
# print(table)
#
# import numpy
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x = numpy.std(speed)
# print(x)
#

#
#
#
#
#
#
#
#

from turtle import Turtle





















# import  pymongo
# myclient=pymongo.MongoClient("mongodb://localhost:27017/")
# print(myclient.list_database_names())
#
# mydb=myclient["form"]
# mycol=mydb["details"]
# mydir={"name":"rocket raja","age":100}
# # data={"age":100}
# que=mycol.find().sort("age",-1)
# for x in que:
#     print(x)

# mydb_list=myclient.list_database_names()
# if "form" in mydb_list:
#     print("Available")












######################MySQl##########################################################################

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="python"
# )
#
# mycursor=mydb.cursor();
# # sql = "INSERT INTO  data(id,name,age) VALUES (%s, %s,%s)"
# # val = (122, "Highway 21",88)
# # mycursor.execute(sql, val)
# #
# # mydb.commit()
# #
# # print(mycursor.rowcount, "record inserted.")
# # mycursor.execute("SELECT * FROM data")
# # for x in mycursor:
# #     print(x)
#
# sql = "SELECT * FROM data ORDER BY age DESC"
#
# mycursor.execute(sql)
# # myresult=mycursor.fetchall()
# for x in mycursor:
#     print(x)
#
# # sql="INSERT INTO homedetails(id,Namw,img) VALUES(%S,%S,%S)"
# # val="(27,selva,hi.jpg)"
# # mycursor.execute(sql,val)
# # mydb.commit()
# # print(mycursor.rowcount,"inserted")
# # mycursor.execute("SELECT * FROM homedetails")
# # for x in mycursor:
# #     print(x)