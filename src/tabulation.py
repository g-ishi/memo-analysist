import configparser

from my_exceprion import UndefinedMarkError


config = configparser.ConfigParser()
config.read('config.ini')


class Tabulation(object):
    """メモからデータを集計するクラス"""
    def __init__(self):
        self.defined_marks = config['DEFINED_MARKS']
        self.count_marks_num = {
            self.defined_marks['done']: 0,
            self.defined_marks['todo']: 0
        }

    def count_marks(self, file):
        """
        記号がそれぞれいくつあるか集計する

        Args:
            file _io.TextIOWrapper:
                読み込み対象ファイルのオブジェクト

        Exceprions:
            UndefinedMarkError:
                定義されていない記号が使われていた場合の例外
        """
        for line in f.readlines():
            if self.defined_marks['done'] in line:
                self.count_marks_num[self.defined_marks['done']] += 1
            elif self.defined_marks['todo'] in line:
                self.count_marks_num[self.defined_marks['todo']] += 1
            else:
                raise UndefinedMarkError
        print(self.count_marks_num)
        

if __name__ == '__main__':
    t = Tabulation()
    print(t.count_marks)

    with open('test.txt', 'r') as f:
        try:
            t.count_marks(f)
        except UndefinedMarkError:
            print('undefined mark appeare!!')
