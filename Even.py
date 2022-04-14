# 自然数のリストを入力すると、そのリストから奇数をすべて削除したリストを出力するプログラムを作成せよ。

from re import I
from sys import int_info

# 偶数のみを取りだす関数
def even(aaa):

# 変数Iの分だけ、もしリストの数字が割り切れる場合だけaaaに格納
    aaa = [i for i in aaa if i % 2 == 0]
    print(aaa)

str = input("X. 好きな数字を入力してください。複数入力する場合は、半角スペースで区切ってください ")

# 変数yを用意し、str.splitで得られた個々の文字をint型に変換する
y = [int(x) for x in str.split()]

# even呼び出し
even(y)