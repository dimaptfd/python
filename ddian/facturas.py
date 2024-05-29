def pagar_factura(clave):
    claves = list(facturas.keys())  
    for clave in claves:  
        facturas.pop(clave)  
    print(facturas)


def abono_factura(abono):
   pasivo = valor_factura - abono
   facturas[factura]= pasivo
   print(f"valor abonado: {abono} \nvalor a pagar: {pasivo}")

def agregar_factura(factura, valor):
   global facturas
   facturas[factura]=valor 

facturas = {}
while True:
    menu = int(input("1 para agregar una factura: \n2 pagar factura: \n3 para terminar operacion: \n:"))
    print("**************************************************************************")
    if menu == 1:
    
        isAppRunning = True
        while isAppRunning:
            factura = str(input("ingrese factura nueva: "))
            if factura == "":
                    isAppRunning=False
                    break
            else:
                    valor_factura = int(input(f"ingrese el coste de la factura {factura}: "))
                    agregar_factura(factura, valor_factura)
                    print("**************************************************************************")

    elif menu == 2:
        menu2 = int(input("1 para pahgar factura: \n2 para abonar factura: "))
        if menu2 == 1:
            factura1 = int(input("ingrese numero de factura a pagar: "))
            pagar_factura(factura1)
            print("**************************************************************************")
        elif menu2 == 2:
            factura = int(input("ingrese numero de factura a abonar: "))
            abono = int(input(f"ingrese valor bono a pagar para la factura {factura}: "))
            abono_factura(abono)
            print("**************************************************************************")
                

    else: 
        print(facturas)
   
        
      

   