import configparser
import numpy as np
from datetime import datetime


from exception import UndefinedMarkError


config = configparser.ConfigParser()
config.read('config.ini')


class Tabulation(object):
    """
    メモからデータを集計するクラス
    規定のフォーマットで書かれたメモから、以下を集計する
        ・status,typeごとの合計時間
    用語：
        <status_mark>[<type>]~~(<time>)
        例）●[ps-lte]朝会(9:23)
    TODO:リファクタリング
        インスタンス変数と一般の変数の使い分けルール
    """
    def __init__(self):
        self.status_marks = config['STATUS_MARKS']
        self.type_delimiter = {
            'start': config['TYPE_DELIMITER']['START'],
            'end': config['TYPE_DELIMITER']['END']
        }
        self.time_delimiter = {
            'start': config['TIME_DELIMITER']['START'],
            'end': config['TIME_DELIMITER']['END']
        }
        # メモの一行を要素ごとに分割する
        self.status_list = []
        self.type_list = []
        self.time_list = []
        # タスクにかかった時間
        self.task_time_list = []

    def append_status_list(self, one_line):
        """
        1行のメモから、タスクステータスを取得して、リストに追加する

        Args:
            one_line (string):
                一行分のメモ文字列
        Returns:
            self.status_list (list):
                メモ内のタスク種別を格納したリスト
        Exception:
        """
        for _mark in self.status_marks.values():
            if _mark in one_line:
                self.status_list.append(_mark)
        return self.status_list

    def append_type_list(self, one_line):
        """
        1行のメモからタスクの種別を取得して、リストに追加する

        Args:
            one_line (string):
                一行分のメモ文字列
        Returns:
            self.type_list (list):
                メモ内のタスク種別を格納したリスト
        Exception:
        """
        # デリミタで分割し、タスクの種別を取得
        _split = one_line.split(self.type_delimiter['start'])[1]
        task_type = _split.split(self.type_delimiter['end'])[0]
        self.type_list.append(task_type)
        return self.type_list

    def append_time_list(self, one_line):
        """
        1行のメモから時間を取得して、配列に格納する
        
        Args:
            one_line (string):
                一行分のメモ文字列
        Returns:
            self.time_list (list):
                メモ内のタスク時間を格納したリスト
        Exception:

        """
        # デリミタで分割し、タスク時間の配列に格納
        _s = one_line.split(self.time_delimiter['start'])[1]
        task_time = _s.split(self.time_delimiter['end'])[0]
        self.time_list.append(task_time)
        return self.time_list

    def append_task_time_list(self, time_list):
        """
        タスクにかかった時間を計算し、配列に格納する。
        Args:
            time_list (list):
                タスクの終了時間のリスト
        Returns:
            self.task_time_list (list):
                メモ内のタスク種別を格納したリスト
        Exception:
        """
        # 始業時間をdatetime型に変換
        _start_time = config['WORKING_TIME']['start_work']
        start_time = datetime.strptime(_start_time, '%H:%M')

        # リスト間の差分で、タスクにかかった時間を計算する
        for _time in time_list:
            target_time = datetime.strptime(_time, '%H:%M')
            # 最初のタスクは始業時間からの差分で求める
            if time_list.index(_time) == 0:
                task_time = target_time - start_time
                self.task_time_list.append(task_time)
                prev_time = target_time
                continue

            task_time = target_time - prev_time
            self.task_time_list.append(task_time)
            prev_time = target_time

        return self.task_time_list

    def collect_status_list(self, status_list):
        """
        status_listから、タスクステータスごとの数を集計する

        Args:
            status_list (list):
                タスクステータスを格納したリスト
        Returns:
            status_numbers (dict):
                タスクステータスの数を集計した辞書
        Exception:
        """
        status_numbers = {}
        for _mark in self.status_marks.values():
            status_numbers[_mark] = status_list.count(_mark)
        return status_numbers

    def collect_type_list(self, type_list):
        """
        type_listから、タスク種別ごとの数を集計する

        Args:
            type_list (list):
                タスク種別を格納したリスト
        Returns:
            type_numbers (list):
                タスク種別ごとの数を集計した辞書
        Exception:
        """
        type_numbers = {}
        for _type in set(type_list):
            type_numbers[_type] = type_list.count(_type)
        return type_numbers

    def reconstract_memo(self):
        """
        status_list,type_list,task_time_listからメモを再構築する。
        
        Args:

        Returns:
            memo_list (list):
                1つの要素が1行のメモに対応するリスト
                それぞれのタスクにかかった時間を集計するために使用する
        Exception:
        """
        memo_list = []
        if not (len(self.status_list) == len(self.type_list)
                == len(self.task_time_list)):
            # TODO:例外処理を行う
            return print('length errror')
        for _status, _type, _task_time\
                in zip(self.status_list, self.type_list, self.task_time_list):
            _memo_line = {
                'status': _status,
                'type': _type,
                'task_time': _task_time
            }
            memo_list.append(_memo_line)
        return memo_list

    def calc_status_time(self, memo_list):
        """
        タスクステータスごとにかかった合計時間の計算を行う

        Args:
            memo_list (list):
                メモの1行を辞書として要素に持つリスト
        Returns:
            status_times (dict):
                タスクステータスごとの合計時間を持つ辞書
        Exception:
        """
        status_times = {}
        for _status in set(self.status_list):
            time_sum = []
            for _line in memo_list:
                if _line['status'] == _status:
                    time_sum.append(_line['task_time'])
            status_times[_status] = np.sum(time_sum)
        return status_times

    def calc_type_time(self, memo_list):
        """
        タスクタイプごとにかかった合計時間の計算を行う

        Args:
            memo_list (list):
                メモの1行を辞書として要素にもつリスト
        Returns:
            type_times (dict):
                タスクタイプごとの合計時間を持つ辞書
        Exception:
        """
        type_times = {}
        for _type in set(self.type_list):
            time_sum = []
            for _line in memo_list:
                if _line['type'] == _type:
                    time_sum.append(_line['task_time'])
            type_times[_type] = np.sum(time_sum)
        return type_times

    def main(self):
        """
        メモを解析し、種別ごとに分類し、それぞれの合計時間を計算する

        Args:
        Returns:
            status_times (dict):
                タスクステータスごとの合計時間を持つ辞書
            type_times (dict):
                タスクタイプごとの合計時間を持つ辞書
        Exception:
        """
        # TODO: 設定ファイルからフォルダの巡回を行うプログラムの作成
        # TODO: 対象ファイルはmain.pyで決めて、それを引数で受け取るようにする、        
        with open('test.txt', 'r') as memo_file:
            for _line in memo_file.readlines():
                self.append_status_list(_line)
                self.append_time_list(_line)
                self.append_type_list(_line)
        
        self.append_task_time_list(self.time_list)
        
        memo_list = self.reconstract_memo()
        status_times = self.calc_status_time(memo_list)
        type_times = self.calc_type_time(memo_list)
        return status_times, type_times


if __name__ == '__main__':
    t = Tabulation()
    # print(t.main())
    with open('test.txt', 'r') as f:
        for line in f.readlines():
            t.append_status_list(line)
            t.append_type_list(line)
            t.append_time_list(line)
    print(t.status_list)
    print(t.type_list)
    print(t.time_list)
    print(t.append_task_time_list(t.time_list))
    print(t.collect_status_list(t.status_list))
    print(t.collect_type_list(t.type_list))
    print(t.calc_status_time(t.reconstract_memo()))
    print(t.calc_type_time(t.reconstract_memo()))
    print(t.main())
