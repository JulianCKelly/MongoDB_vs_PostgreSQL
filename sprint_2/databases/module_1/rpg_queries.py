import sqlite3
from queries import QUERY_LIST


conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


def execute_query(curs, query):
    curs.execute(query)
    return curs.fetchall()


def execute_queries(curs, queries):
    answers = {}
    for index, query in enumerate(queries):
        answers[index] = execute_query(curs, query)
    return answers


if __name__ == '__main__':
    answers = execute_queries(curs, QUERY_LIST)
    for key, value in enumerate(answers.values()):
        print(f"{key}: {value}")
