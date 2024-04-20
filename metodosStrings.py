string1 = "soy hoy Ivan hoy Ivan hoy Ivan hoy Ivan hoy"
string2 = "Hoy soy Pedro"

mayusc = string1.upper()
minusc = string2.lower()
primeraMayusc = string1.capitalize()
#Funcion para poder contar cuantas veces se repite una palabra
contador = 0
indice = 0
ultimoHola = string1.find("hoy")
for i in range(len(string1)):
    buscar = string1.find("hoy",indice+1)
    if(buscar != -1):
        contador += 1
        indice = buscar 
print(contador)
#------------------------#
print(mayusc)
print(minusc)
print(primeraMayusc)
