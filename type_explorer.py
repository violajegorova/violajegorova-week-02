# Pamata tipu izpēte Pythonā
name = "Violeta"
year = 2026
number = 99.99
it_is_hot = False
result = None

#Izvade ar katras vērtības tipu
print(name, type(name))
print(year, type(year))
print(number, type(number))
print(it_is_hot, type(it_is_hot))
print(result, type(result))

#Pārbaude, vai vērtības ir patiesas (truthy) vai nepatiesas (falsy)
print(bool("It is very hot"))       #Netukšs teksts -> True (truthy)
print(bool(""))                     #Tukšs teksts -> False (falsy)
print(bool(42))                     #Netukšs skaitlis -> True (truthy)
print(bool(0))                      #Nulle -> False (falsy)

#Konvertēšana starp tipiem
print(float("5.976"))               #Konvertē tekstu "5.976" uz skaitli 5.976
print(int("57"))                    #Konvertē tekstu "57" uz skaitli 57
print(float("hello"))               #Nevar konvertēt tekstu "hello" uz skaitli, tāpēc tas izraisīs kļūdu (ValueError)
print(str("42"))                    #Konvertē skaitli 42 uz tekstu "42"