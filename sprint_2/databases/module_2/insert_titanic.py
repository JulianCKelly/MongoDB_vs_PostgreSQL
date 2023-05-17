'''PG conn and cur setup'''
from os import getenv
import psycopg2
import pandas as pd

DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')


# make postgres connection and cursor
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                           password=PASSWORD, host=HOST,)
pg_curs = pg_conn.cursor()


def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results


CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic_table(
    passenger_id SERIAL PRIMARY KEY,
    Survived INT NOT NULL,
    Pclass INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Sex VARCHAR(10) NOT NULL,
    Age FLOAT NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL,
    Parents_Children_Aboard INT NOT NULL,
    Fare FLOAT NOT NULL);
'''

DROP_TITANIC_TABLE = '''
    DROP TBALE IF EXISTS titanic_table; ;
'''

df = pd.read_csv('titanic.csv')
# Removing any single quotes in the name column
df['Name'] = df['Name'].str.replace("'", '')

if __name__ == '__main__':
    # Create the table and its associated Schema
    # Drop Table
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    # Create table
    execute_query_pg(pg_curs, pg_conn, CREATE_TITANIC_TABLE)

    records = df.values.tolist()

    for record in records:
        insert_statement = ''' 
            INSERT INTO titanic_table (survived, pclass, name, sex, age,
            siblings_spouses_aboard, parents_children_aboard, fare)
            VALUES {};
        '''.format(tuple(record))
        execute_query_pg(pg_curs, pg_conn, insert_statement)
