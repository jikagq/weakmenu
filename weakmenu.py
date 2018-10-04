# IMPORTS
import csv
# FIN
# VAR GLOBAL
# c = csv.writer(open("menus.csv", "wb"))
# cr = csv.reader(open("menus.csv", "rb"))

fname = "menus.csv"
file = open(fname, "r")
# FIN
# FONCTIONS

# FIN



print("                                 *=========================================*")
print("                                 *                 HELLO THERE             *")
print("                                 *=========================================*")
print("-----------------------------------------------------------------------------------------------------------------")

try:
    reader = csv.reader(file)
    print("ici")
    for row in reader:
        print(row)
finally:
    file.close()
