import matplotlib.pyplot as plt
import numpy as np


class Analysis(object):
    """データの分析・分析結果のグラフ化を行うクラス"""
    def __init__(self):
        pass


if __name__ == '__main__':
    


    sample_data = {'●': 6, '○': 1}
    plt.plot(['●', '○'], [6, 1])
    plt.ylabel('task numbers')
    plt.show()
    objects = ['●', '○']
    values = [6, 1]
    plt.bar(objects, values)
    plt.xticks(objects, values)
    plt.ylabel('task numbers')
    plt.title('task status')
    plt.show()
