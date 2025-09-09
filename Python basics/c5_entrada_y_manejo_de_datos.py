  # --- INGRESO DE DATOS ---
#Se usa la funcion input para ingresar datos y almacenarlo en una variable
name = input("Ingrese su nombre: ")
print(name)
print(type(name))
age_str = input("Ingrese su edad: ")
print(age_str)
print(type(age_str))

# --- CASTING ---
# Aunque ingrese un numero en edad, se comprueba que se almacena como string
# Para convertir el ingreso de un numero en dato numerico se hace un artificio llamado casting
# Con este artificio se cambia el tipo de dato

age_int = int(input("Ingrese su edad: "))
print(age_int)
print(type(age_int))

# Tambien se puede hacer casting a otro tipo de dato
age_flt = float(input("Ingrese su edad: "))
print(age_flt)
print(type(age_flt))

# Si ingresamos un dato con el casting que no concuerde con el tipo de dato, saltara un error de tipo ValueError
