edad = 20
nacionalidad = 'VENEZOLANO'
# if > si, and (y)

if edad > 18 and nacionalidad == 'PERUANO':
    print('Puedes Votar')
    
# else > sino

else:
    print('Llamare a tus padres')
    
# if > si, or (ó)
    
if edad > 18 or nacionalidad == 'PERUANO':
    print('Puedes Votar')
    
# else > sino

else:
    print('Llamare a tus padres')
    
# elif > combinacion de else - if

edad = 13

if edad > 18:
    print('Puedes votar')
elif edad > 15:
    print('Ya te falta poco para votar')
else:
    print('Que haces aquí')
    
# Segun el sexo y la estatura hacer lo siguiente
# si es Masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    # si mide entre 1.30 y 1.49 indicar que si hay ropa
    # si mide menos de 1.30 indicar que no hay prendas
# si es Femenino
    # si mide mas de 1.40 indicar que no hay prendas
    # si mide entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay

sexo = 'Masculino'
estatura = 1.35
# output > SI HAY ROPA

sexo = 'Masculino'
estatura = 1.80
# output > NO HAY ROPA

sexo = 'Femenino'
estatura = 1.20
# output > SI HAY ROPA

sexo = 'Femenino'
estatura = 1.08
# output > NO HAY ROPA

sexo = 'Masculino'
estatura = 1.80
# output > NO HAY ROPA

# if sexo == 'Masculino' and estatura < 1.30 and estatura > 1.50:
#     print('No hay prendas')
# elif sexo == 'Masculino' and estatura >= 1.30 and estatura <= 1.49:
#     print('Si hay ropa')

sexo = 'Femenino'
estatura = 1.45
    
if sexo == 'Masculino':
    if estatura > 1.30 and estatura <1.49:
        print('Si hay ropa')
    else:
        print('No hay Ropa')
elif sexo == 'Femenino':
    # Sexo Femenino
    if estatura > 1.10 and estatura < 1.49:
        print('Si hay ropa')
    else:
        print('No hay ropa')

        # Ó usamos pass o usamos la lógica
        # pass > pasa, no hace nada pero nos permite dejar la condicion vacía
        pass

# OPERADOR TERNARIO
# Condición que sirve para ejecutarse en una sola linea de código y en base a la condicion retornara un valor u otro

# Si el usuario es PERUANO pagará 5 soles, si es EXTRANGERO pagara 8 soles

nacionalidad = 'ECUATORIANO'

if nacionalidad == 'PERUANO':
    print('Paga 5 soles')
else: 
    print('Paga 8 soles')

#       RESULTADO SI ES True if (CONDICIONAL)           else(RESULTADO SI ES False)
resultado = 'Pague 5 soles' if nacionalidad == 'PERUANO' else 'Pague 8 soles'
print(resultado)
    
