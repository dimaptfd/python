mi_diccionario = {
    "object1": 1,
    "object2": 2,
    "object3": 3
}


object = str(input("ingrese valor a eliminar: "))
menos = int(input(" "))
if object in mi_diccionario:
   valor=  mi_diccionario[object]
   valor -= menos
   mi_diccionario[object]=valor
  
print(mi_diccionario)
