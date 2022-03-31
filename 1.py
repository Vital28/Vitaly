import pyttsx3

engine =pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 0.5)

pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
hello = {"Добрый день, сегодня в меню:"}

engine.say(hello)
engine.runAndWait()

menu = "Наполеон, нажмите 1" \
       "Медовик - нажмите 2" \
       "Киевский - нажмите 3"\
       "Если вам ничего не подходит нажмите 4."
engine.say(menu)
engine.runAndWait()

choice_cake = int(input("Какой торт Вы хотели бы приобрести: "))
if choice_cake == 1:
    cake = "наполеон"
elif choice_cake == 2:
    cake = "медовик"
elif choice_cake == 3:
    cake = "киевский"
elif choice_cake == 4:

    voice10 = "приходите еще"

    engine.say(voice10)
    engine.runAndWait()
    breakpoint()



choice = "Хотите узнать состав , нажмите 1" \
         "Хотите узнать цену , нажмите  2" \
         "Хотите узнать остаток, нажмите 3 " \
         "Хотите получить всю информацию о торте, нажмите 4" \
         "Хотите купить торт, нажмите 5" \





engine.say(choice)
engine.runAndWait()



wish = int(input("Что Вы хотели бы уточнить: "))



for k, v in pastry.items():
    if k == cake:
        if wish == 1:
            voice = f"Торт {k} состоит из {v[0]}"
            engine.say(voice)
            engine.runAndWait()

        elif wish == 2:
            voice2 =f"Торт {k} стоит {v[1]} рублей"
            engine.say(voice2)
            engine.runAndWait()
        elif wish == 3:
            voice3 =f"Торт {k} осталось {v[-1]} грамм"
            engine.say(voice3)
            engine.runAndWait()
        elif wish == 4:
            voice4 = f"Торт {k} состоит из {v[0]} , стоит {v[1]} руб, осталось {v[-1]} грамм"
            engine.say(voice4)
            engine.runAndWait()
        elif wish == 5:
            voice5 = "Сколько торта Вам положить"
            engine.say(voice5)
            engine.runAndWait()
            weight = int(input("Сколько торта Вам положить: "))

            voice6 = f"к оплате {pastry[k][1] * weight / 100} рубля"
            engine.say(voice6)
            engine.runAndWait()
            voice7 = f"торта {k} осталось {v[2] - weight} грамм приходите еще"
            engine.say(voice7)
            engine.runAndWait()

