import nacl
import mysql.connector

dataBase = mysql.connector.connect(
    host="198.12.124.54",
    user="joe",
    passwd="Egg.man264.",
    database = "user"
)

cursorObject = dataBase.cursor()

query = "DELETE FROM user_auth WHERE user_id = '1'"
cursorObject.execute(query)


#sql = "INSERT INTO user_auth (email, pwrd_hash) VALUES (%s, %s)"
#val = ("email@email.com", "password")

#cursorObject.execute(sql, val)
dataBase.commit()

dataBase.close()