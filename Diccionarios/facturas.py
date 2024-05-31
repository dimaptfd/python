




def agregar_factura(factura, valor):
   global facturas
   facturas[factura]=valor 

def pagar_factura(key):
   if key in facturas.keys(key):
        del facturas[key]
        print(facturas)

def abono_factura(valor, volos):
   global facturas
   if valor in facturas:
       factura[valor]= quele
       quele -= volos 
       print(f"valor abonado: {abono} \nvalor a pagar: {quele}")


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
                print(facturas)
                print("**************************************************************************")
    elif menu == 2:
        menu2 = int(input("1 para pagar factura: \n2 para abonar factura: "))
        
        if menu2 == 1:
            fac = int(input("ingrese numero de factura: "))
            pagar_factura(fac)
            print("**************************************************************************")
        elif menu2 == 2:
            fac = int(input("ingrese numero de factura: "))
            abono = int(input(f"ingrese valor bono a pagar para la factura {fac}: "))
            abono_factura(fac, abono)
            print(facturas)
            print("**************************************************************************")
    elif menu == 3: 
         break
        
      

      