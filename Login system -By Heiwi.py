import tkinter as tk
import random
import time
import string

backkk = "lightblue"


def delay(delay_time):
    time.sleep(delay_time)


nickname_list = []
password_list = []
key_list = []


def register(nickname=str, password=str):
    global nickname_list, password_list
    if nickname != password:
        nickname_list.append(nickname)
        password_list.append(password)
    else:
        print("Nickname and password cannot be same.")


register("Heiwi", "123456")
register("O1Isyankar","010101")

for qq in range(0, 100):
    Keyyz = ''.join(random.sample(string.ascii_lowercase, 8))
    key_list.append((Keyyz))

Keyy_sayi = random.randint(0, len(key_list) - 1)
Keyy = key_list[Keyy_sayi]

arayuz = tk.Tk()
arayuz.title("Login / Key System -By Heii!")
arayuz.geometry("500x400")
arayuz.configure(bg=backkk)

Void = tk.Label(text=" ", bg=backkk)

kullanici = tk.Label(text="Name : ", font="Arial", bg=backkk)
kullanici.pack()
# kullanici.place(x = 25 , y = 10)

kullanici_adi = tk.StringVar()
kullanici_giris = tk.Entry(textvariable=kullanici_adi)
kullanici_giris.pack()
# kullanici_giris.place(x=10,y=38)

sifre = tk.Label(text="Password : ", font="Arial", bg=backkk)
sifre.pack()
# sifre.place(x = 25 , y = 65)

kullanici_sifre = tk.StringVar()
kullanici_sfr = tk.Entry(textvariable=kullanici_sifre)
kullanici_sfr.pack()
# kullanici_sfr.place(x=10,y=93)

keyy_alma = tk.Label(text=" ", bg=backkk, font="Arial")


# keyy_alma.place(x=150,y=150)

def login_function():
    kullan = kullanici_adi.get()
    sif = kullanici_sifre.get()
    if nickname_list.count(kullan) > 0:
        if password_list.count(sif) > 0:
            print("User {} with password, {} logged in to the system and its key is : {}".format(kullan, sif, Keyy))
            delay(0.1)
            keyy_alma.configure(text=Keyy)
        elif password_list.count(kullan) == 0:
            print("User {} with password {} could not log in to the system. REASON : Password is incorrect.".format(
                kullan, sif))
            keyy_alma.configure(text="Username or password is incorrect.")
    elif nickname_list.count(kullan) == 0:
        keyy_alma.configure(text="Username or password is incorrect.")
        if password_list.count(sif) > 0:
            print("User {} with password {} could not log in to the system. REASON : Nickname is incorrect.".format(
                kullan, sif))
            keyy_alma.configure(text="Username or password is incorrect.")
        else:
            print(
                "User {} with password {} could not log in to the system. REASON : Nickname and password are incorrect".format(
                    kullan, sif))
            keyy_alma.configure(text="Username or password is incorrect.")


Void.pack()

giris = tk.Button(text="Get key", font="Arial", command=login_function)
giris.pack()
# giris.place(x = 47 , y = 93 + (65-38))

keyy_alma.pack()

keyy_lb = tk.Label(text="Key : ", bg=backkk, font="Arial")
keyy_lb.pack()

key = tk.StringVar()
keyy_login = tk.Entry(textvariable=key)
keyy_login.pack()

keyy_dogrulama = tk.Label(text=" ", bg=backkk)
keyy_dogrulama.pack()

Void_2 = tk.Label(text=" ", font="Arial", bg=backkk)
Void_2.pack()


def key_login():
    kullan = kullanici_adi.get()
    sif = kullanici_sifre.get()
    Keyzz = key.get()
    if Keyzz == Keyy:
        print("User {} with password, {} logged in to the system.".format(kullan, sif))
        delay(0.7)
        print("Code finished!")
        arayuz.quit()
    else:
        print(
            "User {} with password {} could not log in to the system. REASON : Key is incorrect. ".format(kullan, sif))
        keyy_dogrulama.configure(text="Key is incorrect.")


keyy_button = tk.Button(text="Check key", font="Arial", command=key_login)
keyy_button.pack()

arayuz.mainloop()
