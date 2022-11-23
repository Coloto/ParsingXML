from bs4 import BeautifulSoup
import lxml
print('Prueba en Python')

with open('Clientes.xml','r') as f:
    data=f.read()
#print(data)

Bs_data=BeautifulSoup(data,'xml')
#print(Bs_data)

telefonos=Bs_data.find_all('telefono')
#print(telefonos)

b_name=Bs_data.find('cliente', {'ID':'C001'})
#print(b_name)

for tag in Bs_data.find_all('cliente', {'ID':'C001'}):
    tag['ciudad'] = 'Madrid'
#print(Bs_data.prettify())

# muestra la descripción de todos los productos por consola. No solo de uno.
# archivo xml de referencia en el siguiente enlace
# https://gist.github.com/Fhernd/6f2aa7527a682f76c165b91fe0e989ee

# Al Café negro le añadimos el precio 9.95

'''with open('CatalogoProductos.xml','r') as f:
    datos=f.read()
print(datos)

Bs_data=BeautifulSoup(data,'xml')
b_name=Bs_data.find('Producto', {'ID':'100001'})

for tag in Bs_data.find_all('Producto', {'ID':'100001'}):
    tag['Precio'] = '9.95'

print(Bs_data.prettify())'''


with open('CatalogoProductos.xml') as f:
    data=f.read()
#print(data)

descripcion=BeautifulSoup(data, 'xml')
#print(descripcion)

poductos=descripcion.find_all('poductos')
#print(poductos)

b_name = descripcion.find('Producto', {'ID':'100001'})
#print(b_name)

for tag in descripcion.find_all('Producto', {'ID':'100001'}):
    tag['precio'] = "9.95"
print(descripcion.prettify())