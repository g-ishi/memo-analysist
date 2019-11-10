import unittest
import datetime


class TabulationTest(unittest.TestCase):
    """
    Tabulationクラスのユニットテストクラス
    """
    def setUp(self):
        import sys
        sys.path.append('../src')
        from tabulation import Tabulation

        self.tab = Tabulation()
        self.file = open('test.txt', 'r')
        
    def tearDown(self):
        self.file.close()

    def test_append_status_list(self):
        """
        append_status_listメソッドの正常時テスト
        """
        # 正しく実行された場合は、このリストができる
        correct_list = ['●', '●', '●', '●', '●', '○', '●']

        file_lines = self.file.readlines()
        for line in file_lines:
            self.tab.append_status_list(line)
        
        self.assertEqual(self.tab.status_list, correct_list)

    def test_append_type_list(self):
        """
        append_type_listメソッドの正常時テスト
        """
        # 正しく実行された場合は、このリストができる
        correct_list = ['ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'other', 'notdefine']

        file_lines = self.file.readlines()
        for line in file_lines:
            self.tab.append_type_list(line)

        self.assertEqual(self.tab.type_list, correct_list)

    def test_append_time_list(self):
        """
        append_time_listメソッドの正常時テスト
        """
        # 正しく実行された場合は、このリストができる
        correct_list = ['9:23', '9:45', '10:23', '11:10', '12:15', '13:15', '16:19']

        file_lines = self.file.readlines()
        for line in file_lines:
            self.tab.append_time_list(line)

        self.assertEqual(self.tab.time_list, correct_list)

    def test_append_task_time_list(self):
        """
        append_task_time_listメソッドの正常時テスト
        """
        # 正しく実行された場合には、このリストができる
        correct_list = [datetime.timedelta(seconds=1380), datetime.timedelta(seconds=1320), datetime.timedelta(seconds=2280), datetime.timedelta(seconds=2820), datetime.timedelta(seconds=3900), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=11040)]

        # 入力を事前に用意する
        time_list = ['9:23', '9:45', '10:23', '11:10', '12:15', '13:15', '16:19']

        self.assertEqual(
            self.tab.append_task_time_list(time_list), correct_list)

    def test_collect_status_list(self):
        """
        collect_status_listメソッドの正常時テスト
        """
        # 正しく実行された場合には、この辞書になる
        correct_dict = {'●': 6, '○': 1}

        # 入力を事前に用意する
        status_list = ['●', '●', '●', '●', '●', '○', '●']

        self.assertEqual(
            self.tab.collect_status_list(status_list), correct_dict)

    def test_collect_type_list(self):
        """
        collect_type_listメソッドの正常時テスト
        """
        # 正しく実行された場合には、この辞書になる
        correct_dict = {'notdefine': 1, 'other': 1, 'ps-lte': 5}

        # 入力を事前に用意する
        type_list = ['ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'other', 'notdefine']

        self.assertEqual(
            self.tab.collect_type_list(type_list), correct_dict)

    def test_reconstract_memo(self):
        """
        reconstract_memoの正常時テスト
        """
        # 正しく実行された場合には、この辞書になる
        correct_list = [{'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=1380)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=1320)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=2280)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=2820)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=3900)}, {'status': '○', 'type': 'other', 'task_time': datetime.timedelta(seconds=3600)}, {'status': '●', 'type': 'notdefine', 'task_time': datetime.timedelta(seconds=11040)}]

        # 入力を事前に用意する
        self.tab.status_list = ['●', '●', '●', '●', '●', '○', '●']
        self.tab.type_list = ['ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'other', 'notdefine']
        self.tab.task_time_list = [datetime.timedelta(seconds=1380), datetime.timedelta(seconds=1320), datetime.timedelta(seconds=2280), datetime.timedelta(seconds=2820), datetime.timedelta(seconds=3900), datetime.timedelta(seconds=3600), datetime.timedelta(seconds=11040)]

        self.assertEqual(
            self.tab.reconstract_memo(), correct_list)

    def test_calc_status_time(self):
        """
        calc_staus_timeメソッドの正常時テスト
        """
        # 正しく実行された場合には、この辞書になる
        correct_dict = {'○': datetime.timedelta(seconds=3600), '●': datetime.timedelta(seconds=22740)}

        # 入力を事前に用意する
        memo_list = [{'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=1380)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=1320)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=2280)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=2820)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=3900)}, {'status': '○', 'type': 'other', 'task_time': datetime.timedelta(seconds=3600)}, {'status': '●', 'type': 'notdefine', 'task_time': datetime.timedelta(seconds=11040)}]
        self.tab.status_list = ['●', '●', '●', '●', '●', '○', '●']

        self.assertEqual(
            self.tab.calc_status_time(memo_list), correct_dict)

    def test_calc_type_time(self):
        """
        calc_type_timeメソッドの正常時テスト
        """
        # 正しく実行された場合には、この辞書になる
        correct_dict = {'other': datetime.timedelta(seconds=3600), 'notdefine': datetime.timedelta(seconds=11040), 'ps-lte': datetime.timedelta(seconds=11700)}

        # 入力を事前に用意する
        memo_list = [{'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=1380)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=1320)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=2280)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=2820)}, {'status': '●', 'type': 'ps-lte', 'task_time': datetime.timedelta(seconds=3900)}, {'status': '○', 'type': 'other', 'task_time': datetime.timedelta(seconds=3600)}, {'status': '●', 'type': 'notdefine', 'task_time': datetime.timedelta(seconds=11040)}]
        self.tab.type_list = ['ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'ps-lte', 'other', 'notdefine']

        self.assertEqual(
            self.tab.calc_type_time(memo_list), correct_dict)

    def test_memo(self):
        """
        mainメソッドの正常時テスト
        """
        correct_tapple = ({'●': datetime.timedelta(seconds=22740), '○': datetime.timedelta(seconds=3600)}, {'notdefine': datetime.timedelta(seconds=11040), 'ps-lte': datetime.timedelta(seconds=11700), 'other': datetime.timedelta(seconds=3600)})

        self.assertEqual(
            self.tab.main(), correct_tapple)


if __name__ == '__main__':
    unittest.main()
