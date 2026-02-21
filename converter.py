# KONSTANTES
KM_TO_MI = 0.621371             # 1 km = 0.621371 miles
KG_TO_LB = 2.20462              # 1 kg = 2.20462 pounds
L_TO_GAL = 0.264172             # 1 liter = 0.264172 gallons
DOLLAR_TO_EURO = 0.8423502     # 1 dollar = 0.84235020 euros

# Pajautā konversijas tipu/virzienu
choice = input("Izvēlies konversiju (km_to_mi, mi_to_km): ").strip().lower()

# Pajautā vērtību
raw_value = input("Ievadi vērtību: ")

# Nepareiza ievade
try:
    value = float(raw_value)
    print(f"Ievadītā vērtība: {value:.2f}")
except ValueError:
    print("Kļūda: Ievadītā vērtība nav skaitlis!")