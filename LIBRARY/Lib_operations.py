import pymsgbox

from Final_UI.LoginPage import mydb
import mysql.connector
from mysql.connector import Error
mycurr = mydb.cursor()
#
# class FileInsert():
#     def convertToBinaryData(self,filename):
#         with open(filename, 'rb') as file:
#             binaryData = file.read()
#         return binaryData
#
#
#     def insertBLOB(self,id, name, file_data):
#         try:
#             sql_insert_blob_query = """ INSERT INTO material
#                               (id, name, file_data) VALUES (%s,%s,%s)"""
#
#
#             file_to_insert = self.convertToBinaryData(file_data)
#
#             # Convert data into tuple format
#             insert_blob_tuple = (id, name, file_to_insert)
#             result = mycurr.execute(sql_insert_blob_query, insert_blob_tuple)
#             mydb.commit()
#             pymsgbox.alert('File Inserted in Database Succesfully!')
#
#         except mysql.connector.Error as error:
#             pymsgbox.alert('Error while pushing the file to database!')
#
#         finally:
#             if (mydb.is_connected()):
#                 mycurr.close()
#                 mydb.close()
#                 pymsgbox.alert('Connection to Database closed!')
#
#
#
# id = input('Enter the Id of the Book : ')
# name = input('Enter the Name of the Book : ')
# file_data = input('Enter the Location of the Book : ')
# a = FileInsert()
# a.insertBLOB(id,name,file_data)

class FileRetrieve():

    def write_file(self,data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def readBLOB(self,id, photo):

        try:

            sql_fetch_blob_query = """SELECT file_data from material where id = %s"""

            mycurr.execute(sql_fetch_blob_query, (id,))
            record = mycurr.fetchall()
            for row in record:
                image = row
                self.write_file(image, photo)

            pymsgbox.alert('Done!')
        except mysql.connector.Error as error:
            pymsgbox.alert("Error while retrieving!")

        finally:
            if (mydb.is_connected()):
                mycurr.close()
                mydb.close()
                pymsgbox.alert("MySQL connection is closed")

b = FileRetrieve()
id = input('Enter the Id of the file : ')
file_loc = input('Enter the location of the file : ')
b.readBLOB(id,file_loc)