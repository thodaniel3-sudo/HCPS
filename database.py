"""
===========================================================
database.py

Hybrid Composite Prediction System (HCPS)

SQLite Database Module

Author: Daniel Thomas
===========================================================
"""

import sqlite3

DATABASE_NAME = "hcps_database.db"


# ---------------------------------------------------------
# Connect to Database
# ---------------------------------------------------------

def connect():

    connection = sqlite3.connect(DATABASE_NAME)

    return connection


# ---------------------------------------------------------
# Create Table
# ---------------------------------------------------------

def create_table():

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS composites (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        sample_name TEXT,


        epoxy_density REAL,
        horn_density REAL,
        cotton_density REAL,
        limestone_density REAL,


        epoxy_percent REAL,
        horn_percent REAL,
        cotton_percent REAL,
        limestone_percent REAL,


        density REAL,


        tensile_strength REAL,

        flexural_strength REAL,

        compressive_strength REAL,

        young_modulus REAL,

        hardness REAL,

        impact_strength REAL,

        penetration_depth REAL


    )
    """)


    connection.commit()

    connection.close()

# ---------------------------------------------------------
# Save Composite Sample
# ---------------------------------------------------------

def save_sample(

    sample_name,

    epoxy_density,
    horn_density,
    cotton_density,
    limestone_density,


    epoxy_percent,
    horn_percent,
    cotton_percent,
    limestone_percent,


    density,


    tensile_strength,

    flexural_strength,

    compressive_strength,

    young_modulus,

    hardness,

    impact_strength,

    penetration_depth


):


    connection = connect()

    cursor = connection.cursor()


    cursor.execute("""


    INSERT INTO composites(


        sample_name,


        epoxy_density,
        horn_density,
        cotton_density,
        limestone_density,


        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent,


        density,


        tensile_strength,

        flexural_strength,

        compressive_strength,

        young_modulus,

        hardness,

        impact_strength,

        penetration_depth


    )


    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)


    """,


    (

        sample_name,


        epoxy_density,
        horn_density,
        cotton_density,
        limestone_density,


        epoxy_percent,
        horn_percent,
        cotton_percent,
        limestone_percent,


        density,


        tensile_strength,

        flexural_strength,

        compressive_strength,

        young_modulus,

        impact_strength,

        flexural_modulus,

    )


    )


    connection.commit()

    connection.close()


# ---------------------------------------------------------
# Load All Samples
# ---------------------------------------------------------

def load_samples():

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""

    SELECT *

    FROM composites

    ORDER BY id

    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


# ---------------------------------------------------------
# Delete Sample
# ---------------------------------------------------------

def delete_sample(sample_id):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM composites WHERE id=?",

        (sample_id,)

    )

    connection.commit()

    connection.close()


# ---------------------------------------------------------
# Search Sample
# ---------------------------------------------------------

def search_sample(sample_name):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute(

        """

        SELECT *

        FROM composites

        WHERE sample_name=?

        """,

        (sample_name,)

    )

    row = cursor.fetchone()

    connection.close()

    return row


# ---------------------------------------------------------
# Update Sample
# ---------------------------------------------------------

def update_density(

    sample_id,

    new_density

):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute(

        """

        UPDATE composites

        SET composite_density=?

        WHERE id=?

        """,

        (

            new_density,

            sample_id

        )

    )

    connection.commit()

    connection.close()


# ---------------------------------------------------------
# Number of Samples
# ---------------------------------------------------------

def total_samples():

    connection = connect()

    cursor = connection.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM composites"

    )

    count = cursor.fetchone()[0]

    connection.close()

    return count


# ---------------------------------------------------------
# End of File
# ---------------------------------------------------------