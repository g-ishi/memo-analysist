import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from datetime import timedelta
from datetime import date


from tabulation import Tabulation


class Analysis(object):
    """データの分析・分析結果のグラフ化を行うクラス"""

    def __init__(self):
        pass

    def create_bar_graph(self, left, height, label_dict):
        """
        棒グラフの作成を行い、作成した棒グラフを画像として保存する

        Args:
            left (list):
                棒グラフのx軸に表示される値のリスト
            height (list):
                棒グラフのy軸に表示される値のリスト
            label_dict (dict):
                棒グラフのタイトル、x軸ラベル、y軸ラベルの値を持つ辞書
        Returns:
        Exception:
        """
        x_label = label_dict.get('x_label', None)
        y_label = label_dict.get('y_label', None)
        graph_title = label_dict.get('graph_title', None)
        file_prefix = label_dict.get('file_prefix', '')
        file_name = file_prefix + str(date.today())

        plt.bar(left, height)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(graph_title)
        plt.grid(True)
        plt.savefig(file_name)

    def status_graph(self, status_times):
        """
        タスクステータスの集計結果から、棒グラフの作成を行う

        Args:
            status_times (dict):
                タスクステータスごとの合計時間を持つ辞書

        """
        _label_dict = {
            'x_label': 'task status',
            'y_label': 'time spent(minutes)',
            'graph_title': 'Time spent for each task status',
            'file_prefix': 'status',
        }

        left = list(status_times.keys())
        height = status_times.values()

        # timedeltaを文字列に変換
        height_str = [_t.total_seconds() / 60 for _t in height]

        self.create_bar_graph(left, height_str, _label_dict)

    def type_graph(self, type_times):
        """
        タスクタイプの集計結果から、棒グラフの作成を行う

        Args:
            type_times (dict):
                 タスクタイプごとの合計時間を持つ辞書

        """
        _label_dict = {
            'x_label': 'task type',
            'y_label': 'time spent(minutes)',
            'graph_title': 'Time spent for each task type',
            'file_prefix': 'type'
        }

        left = list(type_times.keys())
        height = type_times.values()

        # timedeltaを文字列に変換
        height_str = [_t.total_seconds() / 60 for _t in height]

        self.create_bar_graph(left, height_str, _label_dict)


if __name__ == '__main__':
    t = Tabulation()
    status_times, type_times = t.main()
    print(status_times)
    print(type_times)
    a = Analysis()
    a.status_graph(type_times)

    # left = list(status_time.keys())
    # height = status_time.values()
    # timedeltaを文字列の配列に変換
    # height_str = [_timedelta.total_seconds() / 60 for timedelta in height]

    # label_dict = {
    #     'x_label': 'task status',
    #     'y_label': 'time spent(minutes)',
    #     'graph_title': 'Time spent for each task status',
    # }
    # a = Analysis()
    # a.create_bar_graph(left, height_str, label_dict)

    # 秒を60で割って分を出す。デフォルトで変換する関数は用意されていない。
    # _test = timedelta(seconds=3600)
    # print(_test.total_seconds() / 60)
    # print(type(_test.total_seconds()))

    # print(type(list(left)))
    # print(left)
    # print(type(height_str))
    # plt.bar(left, height_str)
    # plt.title('Time spent for each task status')
    # plt.xlabel('task status')
    # plt.ylabel('time spent(minutes)')
    # plt.grid(True)
    # plt.savefig('test.png')
    # 表示だけ非同期でやらせて、プログラムとしては終了してもいいかも。
    # plt.show()

    # sample_data = {'●': 6, '○': 1}
    # plt.plot(['●', '○'], [6, 1])
    # plt.ylabel('task numbers')
    # plt.show()
    # objects = ['●', '○']
    # values = [6, 1]
    # plt.bar(objects, values)
    # plt.xticks(objects, values)
    # plt.ylabel('task numbers')
    # plt.title('task status')
    # plt.show()
