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

    if bmi < 14:
        date = ["ガリ子ちゃんは抱けないぜ","マシュマロボディが好きなんだよ！","肉食って出直してきな"]
        comment_gariko = random.choice(date)
        print(comment_gariko)

    elif 14 <= bmi < 16:
        date = ["モデルさんかい！？", "小枝のような腕だ", "栄養、足りてる？"]
        comment_model = random.choice(date)
        print(comment_model)

    elif 16 <= bmi <18:
        date = ["ええボディしてんな～", "スラッとした足舐めさせてーや", "嬢ちゃん一杯どお？"]
        comment_bijin = random.choice(date)
        print(comment_bijin)

    elif 18 <= bmi < 21:
        date = ["ちょうどええカラダ", "抱かしてや", "ちょっとだけ。ちょっとだけ触らして"]
        comment_nomal = random.choice(date)
        print(comment_nomal)

    elif 21 <= bmi < 23:
        date = ["ムッチリボディやな～", "好きやで。わい、おまんのカラダ。", "ぷにっぷにやな～"]
        comment_muchimuchi = random.choice(date)
        print(comment_muchimuchi)

    elif 23 <= bmi:
        date =["おっぱいがあれば、抱く", "おっぱいがないなら無価値","おっぱい頼み"]
        comment_debu = random.choice(date)
        print(comment_debu)
