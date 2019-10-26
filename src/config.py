import configparser

config = configparser.ConfigParser()
# タスクステータスの定義
config['STATUS_MARKS'] = {
    'done': '●',
    'todo': '○'
}
# タスク種別のデリミタ　例)[ps-lte]
config['TYPE_DELIMITER'] = {
    'START': '[',
    'END': ']'
}
# 時間のデリミタ
config['TIME_DELIMITER'] = {
    'START': '(',
    'END': ')'
}

# 日付のデリミタ
config['DATE_DELIMITER'] = {
    'START': '【',
    'END': '】'
}

# 始業時間
config['WORKING_TIME'] = {
    'start_work': '09:00',
    'end_work': '18:00'
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)
