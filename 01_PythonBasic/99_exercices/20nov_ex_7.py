# palindrom
import copy
def is_palindrom(z):
    x = z
    inv = 0
    while x:
        inv = inv * 10 + x % 10
        x = x // 10

    if z == inv:
        return 0
    else:
        return 1



if __name__ == '__main__':
    nr = int(input("Care este nr tau?\n"))
    if is_palindrom(nr) == 0:
        print("Da")
    else:
        print("Nu")