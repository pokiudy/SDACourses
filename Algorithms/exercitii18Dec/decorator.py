'''
Decorator - asemenator lui builder, principalul scop este modificare
functionalitatii fara a altera originalul.
Se aplica numai pe functii!
- pentru ca o clasa sa fie considerata un decorator trebuie sa indeplineasca:
A. Constructorul sa primeasca ca parametru functia
B. Sa implementeze method __call__ ce este raspunzatoare pentru
alterare
'''

class Capitalized:
    def __init__(self, func):
        self.func = func

    # metoda call este raspunzatoare pentru accesul functie ce trebuie
    # modificata
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)# in cazul nostru devine msg
        return str(result).capitalize()

class WithQuestionMark:
    def __init__(self, func):
        self.func = func

    # metoda call este raspunzatoare pentru accesul functie ce trebuie
    # modificata
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)# in cazul nostru devine msg
        return str(result) + "?"


@Capitalized
@WithQuestionMark
def format_message(msg):
    return msg


if __name__ == "__main__":
    print(format_message("hello"))