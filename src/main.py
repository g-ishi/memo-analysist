from tabulation import Tabulation
from analysis import Analysis

# TODO:あとでコマンド実行できるようにしたいね
if __name__ == '__main__':
    tab = Tabulation()
    ana = Analysis()

    status_times, type_times = tab.main()
    print(type_times)
    print(status_times)
    ana.status_graph(status_times)
    ana.type_graph(type_times)
