import random
def guess_number():
    number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0 

    while True:
        if attempts >= max_attempts:
            print(f"Beidzās mēģinājumi. Skaitlis bija {number}.")
            print(f"Mēģinājumu skaits: {attempts}.")
            ja_velreiz_speles()
            break

        try:
            guess = int(input("Tavs minējums starp 1 un 100: "))
            attempts += 1
            if guess < number:
                print("Par mazu. Mēģini vēlreiz.")
            elif guess > number:
                print("Par lielu. Mēģini vēlreiz.")
            else:
                print(f"Apsveicu! Tu uzminēji skaitli {number} ar {attempts} mēģinājumiem.")
                ja_velreiz_speles()
                break
        except ValueError:
            print("Nepareizs ievads. Lūdzu, ievadi skaitli.")

def ja_velreiz_speles():
    while True:
        play_again = input("Vai vēlies spēlēt vēlreiz? (jā/nē): ").lower()
        if play_again in ("jā", "ja", "j"): 
            guess_number()
            break   
        elif play_again in ("nē", "ne", "n"):
            print("Paldies par spēlēšanu! Uz redzēšanos!")
            break
        else:
            print("Lūdzu, atbildi ar 'jā' vai 'nē'.")

def main():
    print("Laipni lūdzam skaitļu minēšanas spēlē!")
    guess_number()
if __name__ == "__main__":    main()
