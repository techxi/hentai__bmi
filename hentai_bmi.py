import random

while True:
    height = input("身長（ｍ）：")
    if len(height) ==0:
        print("身長くらいいいじゃん。教えてよ。")
    weight = input("体重（ｋｇ）：")
    if len(weight) == 0:
        print("恥ずかしがらずに体重教えてよ。")
        continue
    height = float(height)
    weight = float(weight)
    bmi = weight / (height*height)
    print("あなたのBMIは" + str(bmi) + "です")

    bmis = [[14, ["ガリ子ちゃんは抱けないぜ","マシュマロボディが好きなんだよ！","肉食って出直してきな"]],
            [16, ["モデルさんかい！？", "小枝のような腕だ", "栄養、足りてる？"]],
            [18, ["ええボディしてんな～", "スラッとした足舐めさせてーや", "嬢ちゃん一杯どお？"]],
            [21, ["ちょうどええカラダ", "抱かしてや", "ちょっとだけ。ちょっとだけ触らして"]],
            [23, ["ムッチリボディやな～", "好きやで。わい、おまんのカラダ。", "ぷにっぷにやな～"]],
            [1000000000,["おっぱいがあれば、抱く", "おっぱいがないなら無価値","おっぱい頼み"]]]

    for b, comments in bmis:
        if bmi < b:
            comment = random.choice(comments)
            print(comment)
            break
