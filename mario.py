def main():
    height = get_height()
    for i in range(1, height + 1):
        print("#"*i)

def get_height():
    while True:
        try: # попробуйте
            n = int(input("Height: "))
            if n > 0:
                return n 
        except ValueError: # Кроме
            print("str")
main()
