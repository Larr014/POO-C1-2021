from Auto import * #desde la clase Auto importa todo
auto1 = Auto("rojo",5)
print(f'Auto1 : {auto1.color} {auto1.velocidad} {auto1.aceleracion}')
auto2 = Auto("azul",10)
print(f'Auto2 : {auto2.color} {auto2.velocidad} {auto2.aceleracion}')

auto1.avanzar()
auto1.avanzar()
auto2.avanzar()
print(f'Auto1 : {auto1.color} {auto1.velocidad} {auto1.aceleracion}')
print(f'Auto2 : {auto2.color} {auto2.velocidad} {auto2.aceleracion}')

auto1.frenar()
auto1.frenar()
auto1.frenar()
print(f'Auto1 : {auto1.color} {auto1.velocidad} {auto1.aceleracion} {auto1.ruedas}')
print(f'Auto2 : {auto2.color} {auto2.velocidad} {auto2.aceleracion} {auto2.ruedas}')
auto1.ruedas=10
print(f'Auto1 : {auto1.color} {auto1.velocidad} {auto1.aceleracion} {auto1.ruedas}')
print(f'Auto2 : {auto2.color} {auto2.velocidad} {auto2.aceleracion} {auto2.ruedas}')