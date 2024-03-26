def c2f(t_c):
    t_f = (t_c*1.8) + 32
    return t_f

def main():
    t_c = float(input("섭씨온도를 입력하세요."))
    t_f = c2f(t_c)
    print(f"화씨 온도는 {t_f}도 입니다.")

if __name__=="__main__":
    main()