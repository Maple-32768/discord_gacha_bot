from cs50 import SQL

db = None
database_path = r"./gacha.db";

def pull(user_data):
    return

def wait_user():
    input('続けるにはEnterを押してください')
    return

def actions(user_data):
    while True:
        print('何を実行しますか？')
        print('1. 単発祈願')
        print('2. 10連祈願')
        print('3. n回祈願')
        print('4. ステータスを確認')
        print('\"Q\"を入力して退出')
        strin = str(input())
        if strin.upper() == 'Q':
            break
        elif strin == '1':
            pull(user_data)
            wait_user()
        elif strin == '2':
            for i in range(10):
                pull(user_data)
            wait_user()
        elif strin == '3':
            try:
                n = int(input('何回祈願しますか？'))
                for i in range(n):
                    pull(user_data)
            except ValueError:
                pass
            wait_user()
        elif strin == '4':
            print('ユーザー名: ' + user_data['user_name'])
            print('総祈願回数: ' + str(user_data['total_count']) + '回')
            print('星5確定まで:' + str(user_data['force_5star_at']) + '回')
            print('星4確定まで:' + str(user_data['force_4star_at']) + '回')
            wait_user()

def main():
    user_name = str(input('ユーザー名: '))
    rows = db.execute('SELECT * FROM always WHERE user_name = ?', user_name)
    if len(rows) ==1:
        actions(rows[0])
    else:
        print('ユーザー名が見つかりませんでした\n新しくプロファイルを作成します')
        db.execute('INSERT INTO always(user_name) VALUES(?)', user_name)
        actions(db.execute('SELECT * FROM always WHERE user_name = ?', user_name)[0])
    return

if __name__ == "__main__":
    db = SQL('sqlite:///gacha.db')
    main()
