import random

def choose_word():
    words = ["banan", "ala", "koteczek", "rudy"]
    return random.choice(words)

def start_game():
    word = choose_word()
    zgadniete_litery = []
    niezgadniete_litery = []
    for x in word:
        if x.isalpha():
            niezgadniete_litery.append("_")
        else:
            niezgadniete_litery.append(x)
    return word, zgadniete_litery, niezgadniete_litery

def show_word(word, zgadniete_litery):
    show_word = ""
    for x in word:
        if x.isalpha() and x.lower() in zgadniete_litery:
            show_word += x
        else:
            show_word += "_"
    return show_word

def gues_x():
    while True:
        x = input("Podaj literę: ").lower()
        if len(x) != 1 or not x.isalpha():
            print("zła litera! podaj jedną literkę: ")
        else:
            return x


def main():
    print("Witaj w  Wisielcu!")
    word, zgadniete_litery, niezgadniete_litery = start_game()
    odslonione_slowo = show_word(word, zgadniete_litery)
    lives = 7
    while True:
        print("\n" + odslonione_slowo)
        print("Nieodgadnięte litery: " + ", ".join(niezgadniete_litery))
        print("Liczba żyć: " + str(lives))
        litera = gues_x()
        if litera in zgadniete_litery or litera in niezgadniete_litery:
            print("Już zgadłeś tę literę!")
            continue
        if litera in word.lower():
            zgadniete_litery.append(litera)
            odslonione_slowo = show_word(word, zgadniete_litery)
            if odslonione_slowo == word:
                print("\nBrawo, odgadłeś słowo: " + word)
                break
        else:
            niezgadniete_litery.append(litera)
            lives -= 1
            if lives == 0:
                print("\nPrzegrałeś! Wisielec to: " + word)
                break

main()