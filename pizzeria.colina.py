grande = 580 #comienza los precios de los tamaños
mediana = 430
pequena = 280
ja = 40 #comienza los precios de los ingredientes
ch = 35
pi = 30
dq =40
ac = 57.5
pe =  38.5
sa= 62.5
lista1= []# creo una listas vacias que la lleno con los ingredientes.
i=1 # i y k las uso como contadores
k=0
diccionario= {'ja':'jamon','ch':'Champinones', 'pi':'Pimenton', 'dq':'Doble_queso','ac':'Aceitunas','pe':'Pepperoni','sa':'Salchichon'}


#tarea= 'si'
#while tarea== 'si':
print('PIZZERIA COLINA')
tamano = str(input('Bienvenidos \n Seleccione: \n (G) grande \n (M) Mediana \n (P) Pequeña '))# pregunto por el tamaño de la pizza


invalida = True
while invalida: #creo un bucle que se cumple mientras la opcion elegida no sea la correcta

	 if  tamano== 'g' or tamano=='G' or tamano=='m' or tamano=='M' or tamano=='p' or tamano=='P':
		 invalida= False
		 break
		 
	 else:	
		 print('Opcion invalida')
		 tamano = str(input(' Seleccione (G) grande (M) Mediana  (P) Pequeña '))



if  tamano=='g' or tamano=='G': #asigno el precio al tamaño elegido
	     print('tamano grande seleccionado')
	     subtotal=580
	     tamano='grande'

elif tamano=='m' or tamano=='M':
         print('tamano mediano seleccionado')
         subtotal=430
         tamano='mediana'

elif tamano=='p' or tamano=='P':
        print('tamano pequeno seleccionado')
        subtotal=280
        tamano='pequeña'  


print('Ingredientes: \n jamon (ja) \n Champinones (ch) \n Pimenton (pi) \n Doble queso (dq) \n Aceitunas (ac) \n Pepperoni (pe) \n Salchichon (sa)')#muestro los ingredientes


se = str(input('Indique ingrediente (Enter para terminar):'))# creo una variable para almacenar los ingredientes


hijo = True
while hijo:
  
    if se== 'ja' or se=='ch' or se=='pi' or se=='dq' or se=='ac' or se=='pe' or se=='sa': 
   	   lista1.append(se) #lleno la lista con los ingredientes y la lista va creciendo mientras siga escogiendo ingredientes 
   	   
   	   if se== 'ja':  #voy sumando el total a pagar conforme escoja ingredie
   	             k=k+ja

   	   elif se=='ch':
   	             k=k+ch

   	   elif se=='pi':
   	             k=k+pi

   	   elif se=='dq':
   	             k=k+dq

       #elif se=='ac':
   	             #k=k+ac

   	   elif se=='pe':
   	             k=k+pe

   	   elif se=='sa':
   	             k=k+sa 
   	   se= str(input('Indique ingredientes (Enter para terminar):'))


    else:
   	    hijo= False
   	       
   	   

print('usted selecciono una pizza margarita tamaño:',tamano)
print('con los siguientes ingredientes:',lista1)

cantidad=(input('desea otra pizza (si/no), presione enter para terminar'))


#if cantidad== 'si':
         #i=i+1
         #print('PIZZA NUMERO',i)

#else:
       #tarea= 'no'

total= subtotal+k

print('el pedido tiene un total de 1 pizza por un monto total de:',total)
 
pago=str(input('hay un 50%  de descuento por pagar en efectivo, desea cancelar en efectivo(si/no)'))

if pago=='si':
 	  total=total/2
 	  print('su monto a cancelar en efectico es:',total)

else:
      print('su monto a cancelar es:',total)	 
	     
	
print('GRACIAS POR SU COMPRA REGRESE PRONTO....')

       





