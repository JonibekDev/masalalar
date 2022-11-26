# men son o'ylayman
# kompyuter tahmin qiladi va taqqoslaydi
import random


def guess_number(x):
    print("1 dan 10 gacha son o'ylang, men uni topaman")
    quyi = 1
    yuqori = x

    while True:
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"{taxmin} mening javobim. t, +, -  ")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print("Topdim")




guess_number(10)