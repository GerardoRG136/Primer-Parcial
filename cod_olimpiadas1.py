def multiplicación(a,b):
  x=a*b
  return x

def división(a,b):
  x=(a/b)
  return x
print("Ingresa tu numero 1")
a= int(input())
print("Ingresa tu numero 2")
b= int(input())
print("El resultado de la multiplicación es", multiplicación(a,b), "y el resultado de la división es", división(a,b))
