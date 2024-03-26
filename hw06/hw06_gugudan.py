def gugudan(dan):
    for i in range (1, 10):
        print(f"{dan} * {i} = {dan*i}")

def main():
    dan = int(input("몇단이 궁금하신가요?"))
    gugudan(dan)

if __name__=="__main__":
    main()