from cs50 import SQL


database_path = r"./gacha.db";


def main():
    print("Type user name")
    user_name = str(input())
    db = SQL('sqlite:///gacha.db')
    rows = db.execute('SELECT * FROM always WHERE user_name = ?', user_name)
    if len(rows) ==1:
        print(rows[0])
    else:
        print('not found')
    return

if __name__ == "__main__":
    main()
