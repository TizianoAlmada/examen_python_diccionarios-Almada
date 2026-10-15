tienda={
    "accion": ["Cs2","Fortnite"],
    "terror": ["El terror de la yale"],
    "misterio":["El asesino de la ETec"]
}
cont=0
biblioteca={}
continuar=True
while continuar:
    print("1. Tienda")
    print("2. Jugar un juego")
    print("3. Salir")
    opcion=int(input("Elija la opcion:  "))
    if opcion==1:
        print("TIENDA")
        print("1.Comprar juego")
        print("2.Ingresar un nuevo juego")
        print("3.Volver al menu principal")
        opci2=int(input("Elija la opcion:  "))
        if opci2==1:
            genero=input("Ingrese el genero\n")
            for key in tienda.keys():
                if genero==key:
                    print(f"Las opciones del genero {genero} son: {tienda[genero]}")
                    for juego in tienda[genero]:
                        numero_del_juego=int(input("Ingrese el numero del juego desea comprar"))
                        if numero_del_juego>=0 and numero_del_juego<=len(tienda[genero]):
                            juego=tienda[genero][numero_del_juego]
                            cont=cont+1
                            biblioteca[cont]=juego
                            print(f"compraste el juego{juego}")    
        elif opci2==2:
            genero=int(input("Ingrese el genero del juego que desea ingresar\n"))
            titulo=input("Ingrese el titulo del juego\n")  
    elif opcion==3:
        continuar=False
    else:
        print("Ingrese una opcion valida")
        
       
        
