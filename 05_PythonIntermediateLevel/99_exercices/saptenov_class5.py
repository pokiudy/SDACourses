from datetime import datetime

def before_after_calling(func):
    def wrapper(*args, **kwargs):
        print(f"Timpul initial este {datetime.now().strftime('%H:%M:%S')}.")
        func(*args, **kwargs)
        print(f"Timpul final este: {datetime.now().strftime('%H:%M:%S')}.")

    return wrapper



@before_after_calling
def sum_total(salar):
    a = 0
    for i in range(12344):
        a += salar
    print(f"Salariul anual este de: {a}")

if __name__ == "__main__":
    sum_total(245678)

