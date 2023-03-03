texto=input("Ingrese el texto: ")
texto=texto.lower()
letras=[]
letras.append(input("Ingrese la primera letra de su eleccion: ").lower())
letras.append(input("Ingrese la segunda letra de su eleccion: ").lower())
letras.append(input("Ingrese la tercera letra de su eleccion: ").lower())

print("\n")

cantidad_letras1=texto.count(letras[0])
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f"La letra '{letras[0]}' esta repetida {cantidad_letras1} veces")
print(f"La letra '{letras[1]}' esta repetida {cantidad_letras2} veces")
print(f"La letra '{letras[2]}' esta repetida {cantidad_letras3} veces")

print("\n")

cantidad=texto.split()
print(f"La cantidad de palabras que hay en este texto son: {len(cantidad)}")

print("\n")

print("La primera letra del texto es: ",texto[0])
print("La ultima letra del texto es: ", texto[-1])

print("\n")

cantidad.reverse()
texto_invertido=" ".join(cantidad)
print(f"El texto invertido es '{texto_invertido}'")

buscar="python" in texto
dic={True:"si",False:"no"}
print(f"La palabra 'python' {dic[buscar]} se encuentra en el texto")