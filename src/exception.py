"""memo-analyticsプログラムで発生する独自例外を定義"""


class UndefinedMarkError(Exception):
    """定義されていない記号が見つかった時に発生する例外"""
    pass
