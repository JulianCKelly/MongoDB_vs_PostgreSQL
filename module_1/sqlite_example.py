# Step 0 - import sqlite3
import sqlite3

# step 1 - Connect to the database
# triple-check spelling of database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - make the "cursor"
cursor = connection.cursor()

# step 3 - Write a query
query = 'SELECT character_id,name FROM charactercreator_character;'

# step 4 - Execute the qeury on the cursor and fetch the results
# "pulling the resutls" from the cursor
results = cursor.execute(query).fetchall()

if __name__ == '__main__':
    print(results[:5])