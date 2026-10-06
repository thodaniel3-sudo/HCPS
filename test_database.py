"""
HCPS DATABASE RECORD CHECK
"""

import sqlite3


connection = sqlite3.connect(
    "HCPS_database.db"
)

cursor = connection.cursor()


cursor.execute(
    "SELECT * FROM composites"
)


records = cursor.fetchall()


print("\nHCPS SAVED RECORDS")
print("==================\n")


for row in records:

    print(row)


print("\nTOTAL RECORDS SAVED:")
print(len(records))


connection.close()