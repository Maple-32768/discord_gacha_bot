import sqlite3


database_path = r"./gacha.db";


def main():
    print("Type user name")
    user_name = str(input())
    connection = sqlite3.connect(database_path)
    cur = connection.cursor()
    cur.execute('SELECT * FROM always WHERE user_name = \'' + user_name + '\'')
    print(cur.rowcount)
    return

if __name__ == "__main__":
    main()
