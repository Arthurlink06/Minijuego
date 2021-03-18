intentos = 4
while intentos != 0:    
    print(f"""\nEntras a un cuarto oscuro con dos puertas. Te quedan {intentos} intentos
    ¿Que puerta abres, la #1 o la #2? """)

    puerta = input(">")

    if puerta == "1":
        print("\nHay un oso gigante comiendodse un cheese cake.")
        print("¿Qué harás?")
        print("1. Tomas el cake")
        print("2. Gritale al oso")
        bear = input(">")
        if bear == "1":
            print("\nEl oso te arranca la cara y se la come. ¡Buen trabajo!")
            intentos -= 1
        elif bear == "2":
            print("\nEl oso te arranca las piernas y se las come. !Buen trabajo¡")
            intentos -= 1
        else:
            print(f"\nBueno, seleccionando {bear} es probablemente mejor.")
            print("El oso sale corriendo.")
            intentos -= 1
    elif puerta == "2":
        print("Estas parado en un abismo sin fin, frente a la retina de Cuthulu.")
        print("1. Moras azules")
        print("2. Pinzas amarillas")
        print("3. Entendiendo revólveres gritando melodias")
        locura = input(">")

        if locura == "1" or locura == "2":
            print("Tu cuerpo sobrevive gracias al poder de la mente de una gelatina")
            intentos -= 1
    else:
        print("""\n¡ÉPALE, TIENES QUE SELECCIONAR UNA DE LAS DOS PUERTAS!
        Pierdes un intento por tonto""")
        input("\nPreiona ENTER para continuar....")
        intentos -= 1
print("\n\n\t------------------Ya no te quedan mas intentos------------------")
