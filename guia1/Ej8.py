def numerostep(numero):
   
    numero_str = str(numero)
    
   
    for i in range(1, len(numero_str)):
        if abs(int(numero_str[i]) - int(numero_str[i - 1])) != 1:
            return False 
    
    return True  

num = int(input("Ingrese un número: "))
print(numerostep(num))
