'''
Pentru ca o clasa sa fie considerata interator trebuie obligatoriu sa contine 2 functii:
1. __iter__()
2. __next__()
'''
# fructe = ["banane", "mere", "pere"]
# in momentul in care ceva se poate itera, parcurge inseamna
# ca avem un interator implementat in spate
# for fruct in fructe:
#     print(fruct)
# cum functioneaza un for:
# 1. crearea unui interator:
# fruct = iter(fructe)
# 2. la fiecare iteratie se apleaza in spate functie __next__() ce returneaza urmatorul element
# print(next(fruct))
# print(next(fruct))
# print(next(fruct))
# 3. functia next merge pana la intalnirea expectiei "StopIteration"
# print(next(fruct)) # -> StopIteration
"""
Cu ajutorul design pattern-ului ITERATOR putem itera (parcurge) orice clasa nu doar:
1. List
2. Tuple
3. Set
4. Dictionary
"""
class CosCuFructe:
    def __init__(self):
        self._cos = []
    def append(self, fruct):
        self._cos.append(fruct)
    def __iter__(self):
        '''
        iteratorul este indexul.
        iteratorul incepe de la -1 tot timpul!
        '''
        self.index = -1
        return self
    def __next__(self):
        '''
        primul lucru ce se va intampla dupa crearea iteratorului este apelarea
        functie next! astfel, next aduna cate un 1 la iterator, de aceea incepe
        de la -1 pentru a lua in cosiderare si elementul 0. (-1 + 1 = 0)
        '''
        self.index += 1
        if self.index < len(self._cos):
            # return self._cos[0] = "banane"
            # return self._cos[1] = "mere"
            # return self._cos[2] = "pere"
            # return self._cos[3] = "micsunele"
            return self._cos[self.index]
        else:
            raise StopIteration
if __name__ == "__main__":
    cosCuFructe = CosCuFructe()
    cosCuFructe.append("banane")
    cosCuFructe.append("mere")
    cosCuFructe.append("pere")
    cosCuFructe.append("micsunele")
    for fruct in cosCuFructe:
        print(fruct)


