# Fiind dat un text in limba romana (cu diacritice), sa se scrie o functie care converteste literele cu diacritice in litere fara diacritice, si returneaza textul modificat.

def conv_diacritice(text):
    print(text)
    new_string = ""
    for char in text:
        if char == "ă":
            new_string += "a"
        elif char == "ț":
            new_string += "t"
        elif char == "ș":
            new_string += "s"
        elif char == "â":
            new_string += "a"
        elif char == "î":
            new_string += "i"
        else:
            new_string += char
    return new_string


text = 'a fost un scriitor român format la școala simbolismului literar francez. Este autorul unor volume de versuri și proză scrise în baza unei tehnici unice în literatura română, cu vădite influențe din marii lirici moderni francezi pe care-i admira, dar și, cum spune versul bacovian, „din Eminescu, Heine și Lenau.” La început văzut ca poet minor de critica literară, va cunoaște treptat o receptare favorabilă, mergând până la recunoașterea sa drept cel mai important poet simbolist român și unul dintre cei mai importanți poeți din poezia română modernă.'

print(conv_diacritice(text))


# Altfel de rezolvare


def conv_diac(txt):
    diacritice = {'ă': 'a', 'ș': 's', 'ț': 't', 'î': 'i', 'â': 'a'}
    for lit in txt:
        if lit in diacritice:
            txt = txt.replace(lit, diacritice[lit])
    return txt


text = 'George Bacovia (născut George Andone Vasiliu) n. 4/16 septembrie 1881, Bacău, România – d. 22 mai 1957,[2][3][4][5] București, România) '

print(text)
print(conv_diac(text))