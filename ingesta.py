import boto3
import mysql.connector
import csv

host_name = "172.31.31.4" # IPv4 privada de "MV Bases de Datos"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_employees"  

conn = mysql.connector.connect(host=host_name, port=port_number,
user = user_name, password = password_db, database = database_name)
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
with open("data.csv", "w") as file:
    #Estructura de writerow y writerows sugerida por IA
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])
    writer.writerows(cursor.fetchall())
conn.close()

s3 = boto3.client('s3')
s3.upload_file("data.csv", "rdelapuente-storage", "data.csv")
print("Ingesta completada")