def read_age():
    while True:
        try:
            raw = input("Ievadi savu vecumu: ").strip()
            age = int(raw)  # Pārvērš ievadi par veselu skaitli
            if age < 0:
                print("Vecums nevar būt negatīvs. Mēģini vēlreiz.")
                continue
            if age > 120:
                print("Vecums nevar būt lielāks par 120. Mēģini vēlreiz.")
                continue
            return age
        except ValueError:
            print("Lūdzu, ievadi derīgu skaitli.")
            continue

def to_bool(prompt: str) -> bool:
    yes_values = {"j", "jā", "yes", "y", "true", "t"}
    no_values = {"n", "ne", "no", "nē", "false", "f"}

    while True:
        value = input(f"{prompt} ").strip().lower()

        if value in yes_values:
            return True
        if value in no_values:
            return False
        else:
            print("Lūdzu, ievadi 'jā' vai 'nē'.")

def main() -> None:
    age = read_age()
    print(f"Tavs vecums ir: {age}")

    has_license = to_bool("Vai tev ir autovadītāja apliecība? (jā/nē)")
    print(f"Vai tev ir autovadītāja apliecība? {'Jā' if has_license else 'Nē'}")

    is_student = to_bool("Vai tu esi students? (jā/nē)")
    print(f"Vai tu esi students? {'Jā' if is_student else 'Nē'}")

    is_veteran = to_bool("Vai tu esi veterāns? (jā/nē)")
    print(f"Vai tu esi veterāns? {'Jā' if is_veteran else 'Nē'}")

    can_vote = age >= 18
    can_rent_car = age >= 21 and has_license
    student_discount = (16 <= age <= 26) and is_student
    senior_discount = age >= 65 or is_veteran

    print("--- Rezultāti ---")
    print(f"{'Balsošana':<{LABEL_WIDTH}}{mark(can_vote):>{VALUE_WIDTH}}")
    print(f"{'Auto īre':<{LABEL_WIDTH}}{mark(can_rent_car):>{VALUE_WIDTH}}")
    print(f"{'Studentu atlaide':<{LABEL_WIDTH}}{mark(student_discount):>{VALUE_WIDTH}}")
    print(f"{'Senioru atlaide':<{LABEL_WIDTH}}{mark(senior_discount):>{VALUE_WIDTH}}")

def mark(ok: bool) -> str:
    return "Jā ✓" if ok else "Nē ✗"
LABEL_WIDTH = 20            #kategorijas nosaukums
VALUE_WIDTH = 7             #jā/nē atbilde

if __name__ == "__main__":
    main()