

mi_diccionario = {
    "object1": 1,
    "object2": 2,
    "object3": 3
}
def elminar_object(coso):
    mi_diccionario.pop(coso)
object = str(input("ingrese valor a eliminar: "))
if object in mi_diccionario:
    elminar_object(object)
    print(mi_diccionario)
else:
    print("valor inesistente")