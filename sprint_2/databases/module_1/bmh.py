import sqlite3
import pandas as pd 

# SQLite connection variables
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# load in the CSV to a Pandas DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')

if __name__ == '__main__':
    # turn the dF into a table called 'review'
    df.to_sql('review', conn, if_exists='replace')

    # Query the table to ensure that the data was truly added.
    curs.execute('''SELECT * FROM review;''')
    # print(curs.fetchall())

    # Nature and Shopping both >= 100

    NATURE_SHOPPING = '''
        SELECT COUNT(*) AS greater_100
        FROM review 
        WHERE Nature >= 100 AND Shopping >= 100
    '''
