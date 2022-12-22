from cipher import Cipher


def main():
    cipher = Cipher()
    key = input("\nВведите ключ: ")
    txt = input("Введите сообщение: ")
    enc_txt = cipher.Process(txt, key)
    print("\nЗашифрованное сообщение: ", enc_txt)
    dec_txt = cipher.Process(enc_txt, key)
    print("\nРасшифрованное сообщение: ", dec_txt)


if __name__ == "__main__":
    main()
