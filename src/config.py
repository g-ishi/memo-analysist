import configparser

config = configparser.ConfigParser()
config['DEFINED_MARKS'] = {
    'done': '●',
    'todo': '○'
}


with open('config.ini', 'w') as config_file:
    config.write(config_file)
