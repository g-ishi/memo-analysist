import unittest
import datetime
import os
from datetime import date


class AnalysisTest(unittest.TestCase):
    """
    Analysisクラスのユニットテストクラス
    """

    def setUp(self):
        import sys
        sys.path.append('../src')
        from analysis import Analysis

        self.ana = Analysis()

    def tearDown(self):
        pass

    def test_create_bar_graph(self):
        """
        create_bar_graphメソッドの正常時テスト
        """
        # 入力の事前準備
        label_dict = {
            'x_label': 'task status',
            'y_label': 'time spent(minutes)',
            'graph_title': 'Time spent for each task status',
            'file_prefix': '',
        }
        left = ['notdefine', 'other', 'ps-lte']
        height = [184.0, 60.0, 195.0]
        target_file_name = str(date.today()) + '.png'

        # すでにファイルが存在する場合には削除しておく
        if os.path.isfile(target_file_name):
            os.remove(target_file_name)

        # 棒グラフのファイル作成
        self.ana.create_bar_graph(left, height, label_dict)

        # ファイルが作成されていることを確認する
        self.assertTrue(os.path.isfile(target_file_name))

    def test_status_graph(self):
        """
        status_graphメソッドの正常時テスト
        """
        # 入力の事前準備
        status_times = {'●': datetime.timedelta(
            seconds=22740), '○': datetime.timedelta(seconds=3600)}
        target_file_name = 'status' + str(date.today()) + '.png'

        # テスト対象ファイルが存在する場合は削除する
        if os.path.isfile(target_file_name):
            os.remove(target_file_name)

        # 棒グラフファイルの作成
        self.ana.status_graph(status_times)

        self.assertTrue(os.path.isfile(target_file_name))

    def test_type_graph(self):
        """
        type_graphメソッドの正常時テスト
        """
        # 入力の事前準備
        type_times = {'other': datetime.timedelta(seconds=3600), 'ps-lte': datetime.timedelta(
            seconds=11700), 'notdefine': datetime.timedelta(seconds=11040)}
        target_file_name = 'type' + str(date.today()) + '.png'

        # テスト対象ファイルが存在する場合は削除する
        if os.path.isfile(target_file_name):
            os.remove(target_file_name)

        # 棒グラフの作成
        self.ana.type_graph(type_times)

        self.assertTrue(os.path.isfile(target_file_name))


if __name__ == '__main__':
    unittest.main()
