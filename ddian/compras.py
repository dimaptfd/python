cesta_de_compras = {}

def agragar_producto(prod, valor):
  global cesta_de_compras
  cesta_de_compras[prod] = valor

def eliminar_producto(prod ):
   cesta_de_compras.pop(prod)


while True:
    menu  =  int(input ( "1 para agregar producto al carrito, 2 para eliminar un producto, 3 para ver productos en el carrito, ingresar cualquier otro numero para finalizar y mostrar total a pagar: "))
   
    if menu == 1:
        isAppRunning = True
        while isAppRunning: 
            prod = input("ingresa el producto apra agregar al carrito: ")
            
            if prod == "":
                isAppRunning = False
                break
            else:
                    valor = int(input(f"ingrese el valor de {prod}: "))
                    agragar_producto(prod, valor)   
                    print(cesta_de_compras)
                    print("**********************************************************")
    elif menu == 2:
            print("**********************************************************")
            prod = str(input("que desea eliminar de la lista: "))
            if prod in cesta_de_compras:
                eliminar_producto(prod)
    elif menu == 3:
            print("**********************************************************")
            print(cesta_de_compras)
    else: 
         print("**********************************************************")
         total = sum(cesta_de_compras.values())
         print(f"el total de la compra es igual a: {total} COP")
         break







  
     






